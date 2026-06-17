"""Kullanici rollerini ve yetki kurallarini tek yerde tanimlar."""

from abc import ABC


class BaseUserRole(ABC):
    """Tum kullanici tiplerinin ortak rol ve yetki davranisini tutar."""

    name = "base"
    display_name = "Temel Rol"
    permissions = frozenset()

    def __init__(self, user=None):
        self.user = user

    def can(self, permission):
        return permission in self.permissions

    def menu_items(self):
        return []


class VisitorRole(BaseUserRole):
    """Giris yapmamis ziyaretcinin sadece vitrin islemlerini yapmasini saglar."""

    name = "visitor"
    display_name = "Ziyaretci"
    permissions = frozenset({"view_products", "search_products", "register", "login"})

    def menu_items(self):
        return [
            ("Ana Sayfa", "home"),
            ("Giris", "login"),
            ("Kayit Ol", "register"),
        ]


class CustomerRole(BaseUserRole):
    """Standart musterinin sepet, siparis ve kendi rapor islemlerini tanimlar."""

    name = "customer"
    display_name = "Musteri"
    permissions = frozenset({
        "view_products",
        "search_products",
        "manage_cart",
        "create_order",
        "view_own_orders",
        "view_own_logs",
        "edit_profile",
    })

    def menu_items(self):
        return [
            ("Ana Sayfa", "home"),
            ("Sepet", "cart"),
            ("Siparisler", "orders"),
            ("Raporlarim", "reports"),
            ("Profilim", "profile"),
        ]


class AdminRole(CustomerRole):
    """Admin kullanicinin urun, kullanici ve sistem raporu yetkilerini ekler."""

    name = "admin"
    display_name = "Admin"
    permissions = CustomerRole.permissions | frozenset({
        "manage_products",
        "manage_users",
        "view_all_logs",
        "change_roles",
        "change_user_passwords",
    })

    def menu_items(self):
        return CustomerRole.menu_items(self) + [
            ("Urun Yonetimi", "admin.list_items"),
            ("Kullanici Yonetimi", "admin.list_users"),
            ("Sistem Loglari", "admin.logs"),
        ]


def role_for_user(user):
    """Flask kullanicisina uygun rol nesnesini uretir."""

    if user is None or not getattr(user, "is_authenticated", False):
        return VisitorRole()
    if getattr(user, "admin", False):
        return AdminRole(user)
    return CustomerRole(user)
