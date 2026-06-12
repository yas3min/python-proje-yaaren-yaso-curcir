import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from ..db_models import db, Item
from .forms import AddItemForm, OrderEditForm, EditItemForm
from ..funcs import admin_only

# Admin blueprint'ini oluştur
admin = Blueprint('admin', __name__, url_prefix='/admin')

# Admin paneli ana sayfası (isteğe bağlı, şimdilik ürün ekleme sayfasına yönlendiriyor)
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
                        price_id="price_placeholder") # TODO:
        db.session.add(new_item)
        db.session.commit()
        flash(f"'{new_item.name}' başarıyla eklendi!", "success")
        return redirect(url_for('admin.add_item'))

    return render_template("admin/add_item.html", form=form)