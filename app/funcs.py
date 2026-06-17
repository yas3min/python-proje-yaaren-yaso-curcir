import os, datetime
from flask import render_template, url_for, abort
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
from dotenv import load_dotenv
from .db_models import Log, Order, OrderedItem, db, User
from functools import wraps

load_dotenv()
mail = Mail()

def record_log(user, action):
    """Kullanici islemlerini tarih/saat bilgisiyle veritabanina kaydeder."""
    if not user or not getattr(user, "is_authenticated", False):
        return

    db.session.add(Log(user_id=user.id, action=action))

def fulfill_order(session):
    uid = session.get('client_reference_id')
    if not uid:
        # İstemci referans ID'si eksikse hata günlüğe kaydedilebilir
        return

    current_user = User.query.get(uid)
    if not current_user or not current_user.cart:
        # Kullanıcı bulunamazsa veya sepeti boşsa hata günlüğe kaydedilebilir
        return

    try:
        order = Order(user_id=uid, date=datetime.datetime.now(), status="Siparişiniz Alındı")
        db.session.add(order)
        db.session.flush()  # Sipariş ID'sini almak için

        # Sepet öğelerini siparişe taşı ve sepetten sil
        for cart_item in list(current_user.cart):
            ordered_item = OrderedItem(
                order_id=order.id, 
                item_id=cart_item.item.id, 
                quantity=cart_item.quantity
            )
            db.session.add(ordered_item)
            db.session.delete(cart_item)  # Sepet öğesini doğrudan sil

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        # Webhook için hatayı günlüğe kaydetmek ve yeniden deneme mekanizmasını tetiklemek önemlidir
        raise e

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        from flask_login import current_user
        if not current_user.is_authenticated or not current_user.admin:
            abort(403)
        return func(*args, **kwargs)
    return wrapper
def send_reset_email(user):
    from flask import url_for, current_app
    from itsdangerous import URLSafeTimedSerializer
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    token = s.dumps(user.id, salt='password-reset-salt')
    msg = Message('Sifre Sifirlama Talebi', sender='noreply@demo.com', recipients=[user.email])
    body = 'Sifrenizi sifirlamak icin asagidaki baglantiya tiklayin:\n' + url_for('reset_token', token=token, _external=True) + '\n\nEger bu talebi siz yapmadiysaniz, bu mesaji gormezden gelebilirsiniz. Sifreniz degismeyecektir.\n'
    msg.body = body
    mail.send(msg)
