import csv
import os
from datetime import datetime
from io import StringIO
from flask import Flask, Response, current_app, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from .forms import LoginForm, RegisterForm, UpdateProfileForm, RequestResetForm, ResetPasswordForm, VerifyResetCodeForm
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from .db_models import db, User, Item, Order, OrderedItem, Log, PasswordResetRequest
from .funcs import mail, send_reset_email, record_log
from .user_roles import role_for_user
from dotenv import load_dotenv
from .admin.routes import admin

from werkzeug.utils import secure_filename

load_dotenv()
app = Flask(__name__)
app.register_blueprint(admin)

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DB_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads' # Yüklenen görsellerin kaydedileceği klasör


Bootstrap(app)
db.init_app(app)
mail.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
	db.create_all()
	admin_email = os.environ.get("ADMIN_EMAIL", "admin@aromora.com")
	admin_password = os.environ.get("ADMIN_PASSWORD", "Admin12345")
	admin_user = User.query.filter_by(email=admin_email).first()
	if admin_user is None:
		admin_user = User(
			name="Admin",
			email=admin_email,
			phone="0000000000",
			password=generate_password_hash(admin_password, method='pbkdf2:sha256'),
			admin=True,
			email_confirmed=True,
		)
		db.session.add(admin_user)
		db.session.commit()
	elif not admin_user.admin:
		admin_user.admin = True
		db.session.commit()

@app.context_processor
def inject_now():
	
	return {'now': datetime.utcnow(), 'current_role': role_for_user(current_user)}

@login_manager.user_loader
def load_user(user_id):
	return db.session.get(User, int(user_id))

def sync_uploads_to_products():
    """
    'uploads' klasöründeki yeni görselleri, her biri 0 TL fiyatla ürün olarak veritabanına ekler.
    """
    upload_folder_rel = current_app.config.get('UPLOAD_FOLDER')
    if not upload_folder_rel:
        return 0

    upload_folder_abs = os.path.join(current_app.root_path, upload_folder_rel)

    if not os.path.isdir(upload_folder_abs):
        try:
            os.makedirs(upload_folder_abs)
            flash("'uploads' klasörü oluşturuldu. Ürün olarak eklemek istediğiniz görselleri bu klasöre atabilirsiniz.", "info")
        except OSError:
            return 0

    added_count = 0
    existing_images = {img[0] for img in Item.query.with_entities(Item.image).filter(Item.image.isnot(None)).all()}

    for filename in os.listdir(upload_folder_abs):
        if os.path.isfile(os.path.join(upload_folder_abs, filename)) and filename not in existing_images:
            item_name = os.path.splitext(filename)[0]
            new_item = Item(name=item_name, price=0.0, category="Çeşitli", image=filename, details=f"{item_name} detayı.", price_id=f"local_{item_name}")
            db.session.add(new_item)
            added_count += 1

    if added_count > 0:
        db.session.commit()
    
    return added_count

@app.route("/")
def home():
	page = request.args.get("page", 1, type=int)
	items = Item.query.paginate(page=page, per_page=8)
	return render_template("home.html", items=items)

@app.route("/login", methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		email = form.email.data
		user = User.query.filter_by(email=email).first()
		if user == None:
			flash(f'Bu emaile {email} ait bir hesap bulunamadı!<br> <a href="{url_for("register")}">Kayıt Ol!</a>', 'error')
			return redirect(url_for('login'))
		elif check_password_hash(user.password, form.password.data): # Şifre kontrolü için hash kullanılıyor
			login_user(user)
			record_log(user, "Giris yapildi")
			db.session.commit()
			return redirect(url_for('home')) 
		else:
			flash("email ve ya şifre hatalı", "error")
			return redirect(url_for('login'))
	return render_template("login.html", form=form)

@app.route("/register", methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegisterForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			flash(f"Bu email {user.email} zaten mevcut!!<br> <a href=\"{url_for('login')}\">Giriş yap!</a>", "error")
			return redirect(url_for('register'))
		new_user = User(name=form.name.data,
						email=form.email.data,
						password=generate_password_hash(form.password.data, method='pbkdf2:sha256'), # Şifre hashlenerek kaydediliyor
						phone=form.phone.data,
						admin=False,
						email_confirmed=1,
						)
		db.session.add(new_user)
		db.session.flush()
		record_log(new_user, "Yeni hesap olusturuldu")
		db.session.commit()
		flash('Kayıt İçin Teşekkürler!', 'success')
		return redirect(url_for('login'))
	return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def logout():
	record_log(current_user, "Cikis yapildi")
	db.session.commit()
	logout_user()
	return redirect(url_for('login'))


@app.route("/add/<id>", methods=['POST'])
def add_to_cart(id):
	if not current_user.is_authenticated:
		flash(f'Önce Giriş Yapmalısın!<br> <a href="{url_for("login")}">Giriş Yap!</a>', 'error')
		return redirect(url_for('login'))

	item = Item.query.get(id)
	if not item:
		flash("Eklemeye çalıştığınız ürün bulunamadı.", "error")
		return redirect(request.referrer or url_for('home'))

	if item.price <= 0:
		flash(f"'{item.name}' henüz fiyatlandırılmamış ve sepete eklenemez.", "warning")
		return redirect(request.referrer or url_for('home'))

	if request.method == "POST":
		quantity = request.form.get("quantity", 1, type=int)
		current_user.add_to_cart(id, quantity)
		record_log(current_user, f"Sepete urun eklendi: {item.name} x {quantity}")
		db.session.commit()
		flash(f'''{item.name} Başarıyla sepete eklendi.<a href="{url_for('cart')}">Sepeti Gör!</a>''','success')
		return redirect(url_for('home'))

@app.route("/cart")
@login_required
def cart():
	price = 0
	price_ids = []
	items = []
	quantity = []
	for cart in current_user.cart:
		items.append(cart.item)
		quantity.append(cart.quantity)
		price_id_dict = {
			"price": cart.item.price_id,
			"quantity": cart.quantity,
			}
		price_ids.append(price_id_dict)
		price += cart.item.price*cart.quantity
	return render_template('cart.html', items=items, price=price, price_ids=price_ids, quantity=quantity)

@app.route('/orders')
@login_required
def orders():
	return render_template('orders.html', orders=current_user.orders)

@app.route("/remove/<id>/<quantity>")
@login_required
def remove(id, quantity):
	current_user.remove_from_cart(id, quantity)
	record_log(current_user, f"Sepetten urun cikarildi: urun_id={id}, adet={quantity}")
	db.session.commit()
	return redirect(url_for('cart'))

@app.route('/reports')
@login_required
def reports():
	logs = Log.query.filter_by(user_id=current_user.id).order_by(Log.created_at.desc()).all()
	return render_template('reports.html', logs=logs)

@app.route('/reports/download')
@login_required
def download_report():
	logs = Log.query.filter_by(user_id=current_user.id).order_by(Log.created_at.desc()).all()
	output = StringIO()
	writer = csv.writer(output)
	writer.writerow(["id", "kullanici", "islem", "tarih_saat"])
	for log in logs:
		writer.writerow([log.id, current_user.email, log.action, log.created_at.strftime("%Y-%m-%d %H:%M:%S")])

	record_log(current_user, "Kendi islem raporunu CSV olarak indirdi")
	db.session.commit()
	return Response(
		output.getvalue(),
		mimetype="text/csv",
		headers={"Content-Disposition": "attachment; filename=kullanici_raporu.csv"},
	)

@app.route('/item/<int:id>')
def item(id):
	item = db.session.get(Item, id)
	if item is None:
		abort(404)
	return render_template('item.html', item=item)

@app.route('/search')
def search():
	query = request.args.get('query', '')
	search = f"%{query}%"
	page = request.args.get('page', 1, type=int)
	items = Item.query.filter(Item.name.like(search)).paginate(page=page, per_page=8)
	return render_template('home.html', items=items, search=True, query=query)

@app.route('/payment_success')
def payment_success():
	return render_template('success.html')


@app.route('/create-order', methods=['POST'], endpoint='create_checkout_session')
def create_order():
    if not current_user.is_authenticated:
        flash("Lütfen önce giriş yapın.", "error")
        return redirect(url_for('login'))
    
    if not current_user.cart:
        flash("Sipariş oluşturmak için sepetinizde ürün olmalıdır.", "warning")
        return redirect(url_for('cart'))

    try:
        order = Order(user_id=current_user.id, date=datetime.now(), status="Siparişiniz Alındı")
        db.session.add(order)
        db.session.flush()  # Sipariş ID'sini almak için veritabanına gönder

        # Sepetteki ürünleri kopyala, siparişe ekle ve sepetten sil
        cart_items_to_process = list(current_user.cart)
        for cart_item in cart_items_to_process:
            ordered_item = OrderedItem(
                order_id=order.id,
                item_id=cart_item.item.id,
                quantity=cart_item.quantity
            )
            db.session.add(ordered_item)
            record_log(current_user, f"Siparis kalemi olusturuldu: #{order.id}, urun_id={cart_item.item.id}, adet={cart_item.quantity}")
            db.session.delete(cart_item)  # Orijinal sepet öğesini sil

        db.session.commit()
        flash("Siparişiniz başarıyla alındı.", "success")
        return redirect(url_for('payment_success'))
    except Exception as e:
        db.session.rollback()
        flash(f"Sipariş oluşturulurken bir hata oluştu: {e}", "error")
        return redirect(url_for('cart'))
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone = form.phone.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        record_log(current_user, "Profil bilgileri guncellendi")
        db.session.commit()
        flash('Hesap bilgileriniz guncellendi!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.phone.data = current_user.phone
        form.email.data = current_user.email
    return render_template('profile.html', form=form)

import string, random

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # Rastgele 6 haneli kod olustur
            code = ''.join(random.choices(string.digits, k=6))
            # Eski istekleri sil
            PasswordResetRequest.query.filter_by(user_id=user.id).delete()
            # Yeni istek olustur
            reset_req = PasswordResetRequest(user_id=user.id, code=code)
            db.session.add(reset_req)
            db.session.commit()
            record_log(user, "Sifre sifirlama talebi olusturuldu (Admin onayli)")
        
        flash('Şifre sıfırlama talebiniz alınmıştır. Şifre sıfırlama kodunuz admin onayına düşmüştür. Lütfen admin ile iletişime geçin.', 'info')
        return redirect(url_for('verify_reset_code'))
    return render_template('reset_request.html', form=form)

@app.route('/reset_password/verify', methods=['GET', 'POST'])
def verify_reset_code():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = VerifyResetCodeForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            reset_req = PasswordResetRequest.query.filter_by(user_id=user.id, code=form.code.data).first()
            if reset_req:
                # Kod dogru, sifreyi guncelle
                user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
                # Istegi sil
                db.session.delete(reset_req)
                record_log(user, "Sifre kod ile basariyla sifirlandi")
                db.session.commit()
                flash('Şifreniz başarıyla güncellendi! Şimdi giriş yapabilirsiniz.', 'success')
                return redirect(url_for('login'))
        flash('Geçersiz email veya doğrulama kodu.', 'error')
        return redirect(url_for('verify_reset_code'))
    return render_template('verify_reset.html', form=form)
