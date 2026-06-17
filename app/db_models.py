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

    admin = db.Column(db.Boolean, default=False)
    email_confirmed = db.Column(db.Boolean, default=False)

    # relations
    cart = db.relationship("Cart", backref="buyer", lazy=True, cascade="all, delete-orphan")
    orders = db.relationship("Order", backref="customer", lazy=True, cascade="all, delete-orphan")
    logs = db.relationship("Log", backref="user", lazy=True, cascade="all, delete")

    @property
    def role(self):
        return "admin" if self.admin else "customer"

    @role.setter
    def role(self, value):
        self.admin = value == "admin"

    @property
    def role_profile(self):
        from .user_roles import role_for_user
        return role_for_user(self)

    def can(self, permission):
        return self.role_profile.can(permission)

    def add_to_cart(self, item_id, quantity=1):
        quantity = max(int(quantity), 1)
        item_id = int(item_id)
        cart_item = Cart.query.filter_by(user_id=self.id, item_id=item_id).first()

        if cart_item:
            cart_item.quantity += quantity
        else:
            db.session.add(Cart(user_id=self.id, item_id=item_id, quantity=quantity))

        db.session.commit()

    def remove_from_cart(self, item_id, quantity=None):
        item_id = int(item_id)
        cart_item = Cart.query.filter_by(user_id=self.id, item_id=item_id).first()
        if not cart_item:
            return

        remove_quantity = cart_item.quantity if quantity is None else int(quantity)
        if remove_quantity >= cart_item.quantity:
            db.session.delete(cart_item)
        else:
            cart_item.quantity -= remove_quantity

        db.session.commit()


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

    user_id = db.Column("uid", db.Integer, db.ForeignKey("users.id"), nullable=False)
    item_id = db.Column("itemid", db.Integer, db.ForeignKey("items.id"), nullable=False)

    quantity = db.Column(db.Integer, default=1)


# =====================
# ORDER
# =====================
class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column("uid", db.Integer, db.ForeignKey("users.id"), nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="pending")

    items = db.relationship("OrderedItem", backref="order", cascade="all, delete-orphan")


# =====================
# ORDER ITEM
# =====================
class OrderedItem(db.Model):
    __tablename__ = "ordered_items"

    id = db.Column(db.Integer, primary_key=True)

    order_id = db.Column("oid", db.Integer, db.ForeignKey("orders.id"), nullable=False)
    item_id = db.Column("itemid", db.Integer, db.ForeignKey("items.id"), nullable=False)

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

# =====================
# PASSWORD RESET REQUEST
# =====================
class PasswordResetRequest(db.Model):
    __tablename__ = "password_resets"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("password_resets", cascade="all, delete-orphan", lazy=True))
