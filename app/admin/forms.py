from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import FloatField, PasswordField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class AddItemForm(FlaskForm):
    name = StringField("Urun Adi", validators=[DataRequired()])
    price = FloatField("Fiyat", validators=[DataRequired()])
    category = StringField("Kategori", validators=[DataRequired()])
    details = TextAreaField("Detaylar", validators=[DataRequired()])
    image = FileField("Urun Gorseli", validators=[FileAllowed(["jpg", "png", "jpeg", "gif"], "Sadece resim dosyalari!")])
    submit = SubmitField("Urun Ekle")


class EditItemForm(FlaskForm):
    name = StringField("Urun Adi", validators=[DataRequired()])
    price = FloatField("Fiyat", validators=[DataRequired()])
    category = StringField("Kategori", validators=[DataRequired()])
    details = TextAreaField("Detaylar", validators=[DataRequired()])
    image = FileField("Yeni Urun Gorseli", validators=[FileAllowed(["jpg", "png", "jpeg", "gif"], "Sadece resim dosyalari!")])
    submit = SubmitField("Urunu Guncelle")


class OrderEditForm(FlaskForm):
    status = SelectField(
        "Siparis Durumu",
        choices=[
            ("Siparisiniz Alindi", "Siparisiniz Alindi"),
            ("Hazirlaniyor", "Hazirlaniyor"),
            ("Kargoya Verildi", "Kargoya Verildi"),
            ("Teslim Edildi", "Teslim Edildi"),
        ],
    )
    submit = SubmitField("Durumu Guncelle")


class AdminPasswordForm(FlaskForm):
    password = PasswordField("Yeni Sifre", validators=[DataRequired(), Length(min=8, max=30)])
    confirm = PasswordField("Yeni Sifre Tekrar", validators=[DataRequired(), EqualTo("password", message="Sifreler eslesmiyor.")])
    submit = SubmitField("Sifreyi Guncelle")
