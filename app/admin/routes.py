import csv
import os
from io import StringIO
from flask import Blueprint, Response, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from ..db_models import db, Item, Log, User, PasswordResetRequest
from .forms import AddItemForm, AdminPasswordForm, OrderEditForm, EditItemForm
from ..funcs import admin_only, record_log

# Admin blueprint'ini oluştur
admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route("/")
@login_required
@admin_only
def dashboard():
    return redirect(url_for('admin.list_items'))

# Ürün listeleme rotası
@admin.route("/items")
@login_required
@admin_only
def list_items():
    items = Item.query.all()
    return render_template("admin/items.html", items=items)

@admin.route("/users")
@login_required
@admin_only
def list_users():
    users = User.query.order_by(User.admin.desc(), User.id.asc()).all()
    return render_template("admin/users.html", users=users)

@admin.route("/users/<int:id>/password", methods=["GET", "POST"])
@login_required
@admin_only
def change_user_password(id):
    user = User.query.get_or_404(id)
    form = AdminPasswordForm()
    if form.validate_on_submit():
        user.password = generate_password_hash(form.password.data, method="pbkdf2:sha256")
        record_log(current_user, f"Kullanici sifresi admin tarafindan degistirildi: {user.email}")
        db.session.commit()
        flash(f"{user.email} icin sifre guncellendi.", "success")
        return redirect(url_for("admin.list_users"))
    return render_template("admin/change_password.html", form=form, user=user)

@admin.route("/password-resets")
@login_required
@admin_only
def password_resets():
    requests = PasswordResetRequest.query.order_by(PasswordResetRequest.created_at.desc()).all()
    return render_template("admin/password_resets.html", requests=requests)

@admin.route("/logs")
@login_required
@admin_only
def logs():
    user_id = request.args.get("user_id", type=int)
    users = User.query.order_by(User.email.asc()).all()
    query = Log.query.join(User).order_by(Log.created_at.desc())
    if user_id:
        query = query.filter(Log.user_id == user_id)
    logs = query.limit(300).all()
    return render_template("admin/logs.html", logs=logs, users=users, selected_user_id=user_id)

@admin.route("/logs/download")
@login_required
@admin_only
def download_logs():
    user_id = request.args.get("user_id", type=int)
    query = Log.query.join(User).order_by(Log.created_at.desc())
    if user_id:
        query = query.filter(Log.user_id == user_id)

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "kullanici", "rol", "islem", "tarih_saat"])
    for log in query.all():
        writer.writerow([
            log.id,
            log.user.email,
            log.user.role,
            log.action,
            log.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        ])

    record_log(current_user, "Admin sistem loglarini CSV olarak indirdi")
    db.session.commit()
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=sistem_loglari.csv"},
    )

@admin.route("/users/<int:id>/toggle-admin", methods=["POST"])
@login_required
@admin_only
def toggle_admin(id):
    user = User.query.get_or_404(id)
    if user.id == current_user.id:
        flash("Kendi admin yetkinizi buradan kaldıramazsınız.", "warning")
        return redirect(url_for("admin.list_users"))

    user.admin = not user.admin
    record_log(current_user, f"Kullanici yetkisi guncellendi: {user.email} -> {user.role}")
    db.session.commit()
    flash(f"{user.email} için yetki güncellendi.", "success")
    return redirect(url_for("admin.list_users"))

@admin.route("/users/<int:id>/delete", methods=["POST"])
@login_required
@admin_only
def delete_user(id):
    user = User.query.get_or_404(id)
    if user.id == current_user.id:
        flash("Kendi hesabınızı buradan silemezsiniz.", "warning")
        return redirect(url_for("admin.list_users"))

    record_log(current_user, f"Kullanici silindi: {user.email}")
    db.session.delete(user)
    db.session.commit()
    flash(f"{user.email} silindi.", "success")
    return redirect(url_for("admin.list_users"))

# Ürün düzenleme rotası
@admin.route("/edit-item/<int:id>", methods=["GET", "POST"])
@login_required
@admin_only
def edit_item(id):
    item = Item.query.get_or_404(id)
    form = EditItemForm(obj=item)

    if form.validate_on_submit():
        if form.image.data and hasattr(form.image.data, 'filename') and form.image.data.filename:
            filename = secure_filename(form.image.data.filename)
            upload_dir = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_dir, exist_ok=True)
            filepath = os.path.join(upload_dir, filename)
            form.image.data.save(filepath)
            item.image = filename

        item.name = form.name.data
        item.price = form.price.data
        item.category = form.category.data
        item.details = form.details.data

        record_log(current_user, f"Urun guncellendi: {item.name}")
        db.session.commit()
        flash(f"'{item.name}' başarıyla güncellendi!", "success")
        return redirect(url_for('admin.list_items'))

    return render_template("admin/edit_item.html", form=form, item=item)

# Ürün silme rotası
@admin.route("/delete-item/<int:id>", methods=["POST"])
@login_required
@admin_only
def delete_item(id):
    item = Item.query.get_or_404(id)
    record_log(current_user, f"Urun silindi: {item.name}")
    db.session.delete(item)
    db.session.commit()
    flash(f"'{item.name}' başarıyla silindi!", "success")
    return redirect(url_for('admin.list_items'))

# Ürün ekleme rotası
@admin.route("/add-item", methods=["GET", "POST"])
@login_required
@admin_only
def add_item():
    form = AddItemForm()

    if form.validate_on_submit():
        # Eğer resim yüklenmezse kullanılacak varsayılan dosya adı
        filename = "default.png"
        
        if form.image.data and hasattr(form.image.data, 'filename') and form.image.data.filename:
            filename = secure_filename(form.image.data.filename)
            upload_dir = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])
            os.makedirs(upload_dir, exist_ok=True)
            filepath = os.path.join(upload_dir, filename)
            form.image.data.save(filepath)

        new_item = Item(name=form.name.data,
                        price=form.price.data,
                        category=form.category.data,
                        image=filename,
                        details=form.details.data,
                        price_id=f"local_{secure_filename(form.name.data)}")
        db.session.add(new_item)
        record_log(current_user, f"Urun eklendi: {new_item.name}")
        db.session.commit()
        flash(f"'{new_item.name}' başarıyla eklendi!", "success")
        return redirect(url_for('admin.add_item'))

    return render_template("admin/add_item.html", form=form)
