import os
from datetime import datetime
from flask import Flask, current_app, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from .forms import LoginForm, RegisterForm, UpdateProfileForm, RequestResetForm, ResetPasswordForm
from itsdangerous import URLSafeTimedSerializer
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from .db_models import db, User, Item, Order, OrderedItem
from .funcs import mail, send_reset_email
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

@app.context_processor
def inject_now():
	
	return {'now': datetime.utcnow()}

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

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
            new_item = Item(name=item_name, price=0.0, category="Çeşitli", image=filename, details=f"{item_name} detayı.", price_id="price_placeholder")
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
						admin=form.isAdmin.data,
						email_confirmed=1,
						)
		db.session.add(new_user)
		db.session.commit()
		flash('Kayıt İçin Teşekkürler!', 'success')
		return redirect(url_for('login'))
	return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def logout():
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
		quantity = request.form["quantity"]
		current_user.add_to_cart(id, quantity)
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
	return redirect(url_for('cart'))

@app.route('/item/<int:id>')
def item(id):
	item = Item.query.get(id)
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
        uid = current_user.id
        order = Order(uid=uid, date=datetime.now(), status="Siparişiniz Alındı")
        db.session.add(order)
        db.session.flush()  # Sipariş ID'sini almak için veritabanına gönder

        # Sepetteki ürünleri kopyala, siparişe ekle ve sepetten sil
        cart_items_to_process = list(current_user.cart)
        for cart_item in cart_items_to_process:
            ordered_item = Ordered_item(
                oid=order.id,
                itemid=cart_item.item.id,
                quantity=cart_item.quantity
            )
            db.session.add(ordered_item)
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
        db.session.commit()
        flash('Hesap bilgileriniz guncellendi!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.phone.data = current_user.phone
        form.email.data = current_user.email
    return render_template('profile.html', form=form)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        flash('Sifrenizi sifirlamak icin e-posta adresinize bir baglanti gonderildi.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, salt='password-reset-salt', max_age=3600)
    except:
        flash('Sifre sifirlama baglantisi gecersiz veya suresi dolmus.', 'error')
        return redirect(url_for('reset_request'))
    user = User.query.get(user_id)
    if user is None:
        flash('Gecersiz kullanici.', 'error')
        return redirect(url_for('register'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        db.session.commit()
        flash('Sifreniz basariyla guncellendi! Simdi giris yapabilirsiniz.', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', form=form)
