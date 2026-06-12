from app.db_models import db, Log


# =========================
# GENEL LOG FONKSİYONU
# =========================
def create_log(user_id, action):
    """
    Sistemde yapılan tüm işlemleri loglar.
    """

    log = Log(
        user_id=user_id,
        action=action
    )

    db.session.add(log)
    db.session.commit()


# =========================
# HAZIR KULLANIM FONKSİYONLARI
# (İSTEĞE BAĞLI AMA ÖNERİLİR)
# =========================

def log_login(user_id):
    create_log(user_id, "Sisteme giriş yaptı")


def log_logout(user_id):
    create_log(user_id, "Sistemden çıkış yaptı")


def log_register(user_id):
    create_log(user_id, "Yeni hesap oluşturdu")


def log_add_to_cart(user_id, item_id):
    create_log(user_id, f"Sepete ürün ekledi (Item ID: {item_id})")


def log_remove_from_cart(user_id, item_id):
    create_log(user_id, f"Sepetten ürün sildi (Item ID: {item_id})")


def log_order(user_id, order_id):
    create_log(user_id, f"Sipariş oluşturdu (Order ID: {order_id})")


def log_product_add(user_id, product_name):
    create_log(user_id, f"Ürün eklendi: {product_name}")


def log_product_delete(user_id, product_name):
    create_log(user_id, f"Ürün silindi: {product_name}")

from app.db_models import db, Log


def create_log(user_id, action):
    log = Log(user_id=user_id, action=action)
    db.session.add(log)
    db.session.commit()    