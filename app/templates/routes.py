from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from functools import wraps

from app import app
from app.db_models import db, Item, User, Log
from app.logger import create_log


# =========================
# STAFF CONTROL
# =========================
def staff_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if current_user.role not in ["admin", "staff"]:
            return "Yetkin yok", 403

        return func(*args, **kwargs)

    return wrapper


# =========================
# ADMIN LOGS
# =========================
@app.route("/admin-logs")
@login_required
def admin_logs():

    if current_user.role != "admin":
        return "Yetkin yok", 403

    logs = Log.query.order_by(Log.created_at.desc()).all()

    return render_template("admin_logs.html", logs=logs)


# =========================
# ADMIN USERS
# =========================
@app.route("/admin/users")
@login_required
def admin_users():

    if current_user.role != "admin":
        return "Yetkin yok", 403

    users = User.query.all()

    return render_template("admin_users.html", users=users)


# =========================
# ROLE CHANGE
# =========================
@app.route("/admin/change-role/<int:user_id>/<role>")
@login_required
def change_role(user_id, role):

    if current_user.role != "admin":
        return "Yetkin yok", 403

    user = db.session.get(User, user_id)
    user.role = role

    db.session.commit()

    return redirect(url_for("admin_users"))


# =========================
# ADD ITEM (REAL)
# =========================
@app.route("/add-item", methods=["GET", "POST"])
@login_required
@staff_required
def add_item():

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]

        item = Item(
            name=name,
            price=float(price)
        )

        db.session.add(item)
        db.session.commit()

        create_log(current_user.id, "Ürün ekledi")

        return redirect(url_for("admin_users"))

    return '''
    <form method="POST">
        <input name="name" placeholder="Ürün adı">
        <input name="price" placeholder="Fiyat">
        <button type="submit">Ekle</button>
    </form>
    '''


# =========================
# DELETE ITEM (REAL)
# =========================
@app.route("/delete-item/<int:id>")
@login_required
@staff_required
def delete_item(id):

    item = Item.query.get(id)

    db.session.delete(item)
    db.session.commit()

    create_log(current_user.id, "Ürün sildi")

    return redirect(url_for("admin_users"))