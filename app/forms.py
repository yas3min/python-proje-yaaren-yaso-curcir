from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, Optional

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Sifre", validators=[DataRequired()])
    submit = SubmitField("Giris yap")

class RegisterForm(FlaskForm):
    name = StringField("Ad:", validators=[DataRequired(), Length(max=50)])
    phone = StringField("Telefon:", validators=[DataRequired(), Length(max=30)])
    email = StringField("E-Mail:", validators=[DataRequired(), Email()])
    password = PasswordField("Sifre:", validators=[DataRequired(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message="Sifre 8-30 karakter arasinda olmali ve sadece harf, rakam ve ozel karakterler icermelidir.")])
    confirm = PasswordField("Sifreyi Onayla:",validators=[EqualTo("password", message="Sifreler eslesmiyor!")])
    isAdmin = BooleanField("Kullaniciyi Admin Yap", default=False)
    submit = SubmitField("Kayit Ol")

class UpdateProfileForm(FlaskForm):
    name = StringField("Ad:", validators=[DataRequired(), Length(max=50)])
    phone = StringField("Telefon:", validators=[DataRequired(), Length(max=30)])
    email = StringField("E-Mail:", validators=[DataRequired(), Email()])
    password = PasswordField("Yeni Sifre (Degistirmek istemiyorsaniz bos birakin):", validators=[Optional(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message="Sifre 8-30 karakter arasinda olmali ve sadece harf, rakam ve ozel karakterler icermelidir.")])
    confirm = PasswordField("Yeni Sifreyi Onayla:", validators=[EqualTo("password", message="Sifreler eslesmiyor!")])
    submit = SubmitField("Bilgilerimi Guncelle")

class RequestResetForm(FlaskForm):
    email = StringField("E-Mail:", validators=[DataRequired(), Email()])
    submit = SubmitField("Sifre Sifirlama Baglantisi Gonder")

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Yeni Sifre:", validators=[DataRequired(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message="Sifre 8-30 karakter arasinda olmali ve sadece harf, rakam ve ozel karakterler icermelidir.")])
    confirm = PasswordField("Yeni Sifreyi Onayla:", validators=[EqualTo("password", message="Sifreler eslesmiyor!")])
    submit = SubmitField("Sifremi Sifirla")
