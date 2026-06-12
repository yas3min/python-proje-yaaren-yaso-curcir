from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# =====================
# USER
# =====================
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="user")  # admin / staff / user
    email_confirmed = db.Column(db.Boolean, default=False)

    # relations
    cart = db.relationship("Cart", backref="buyer", lazy=True)
    orders = db.relationship("Order", backref="customer", lazy=True)
    logs = db.relationship("Log", backref="user", lazy=True, cascade="all, delete")


# =====================
# ITEM
# =====================
class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(250), default="default.png")
    details = db.Column(db.String(250), nullable=False)
    price_id = db.Column(db.String(250), nullable=False)

    orders = db.relationship("OrderedItem", backref="item", cascade="all, delete-orphan")
    in_cart = db.relationship("Cart", backref="item", cascade="all, delete-orphan")


# =====================
# CART
# =====================
class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)

    quantity = db.Column(db.Integer, default=1)


# =====================
# ORDER
# =====================
class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="pending")

    items = db.relationship("OrderedItem", backref="order", cascade="all, delete-orphan")


# =====================
# ORDER ITEM
# =====================
class OrderedItem(db.Model):
    __tablename__ = "ordered_items"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)


# =====================
# LOG
# =====================
class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    action = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)