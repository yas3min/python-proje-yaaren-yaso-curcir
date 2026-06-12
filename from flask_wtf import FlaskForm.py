from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, Optional


class LoginForm(FlaskForm):
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Şifre", validators=[DataRequired()])
	submit = SubmitField("Giriş yap")

class RegisterForm(FlaskForm):
	name = StringField("Ad:", validators=[DataRequired(), Length(max=50)])
	phone = StringField("Telefon:", validators=[DataRequired(), Length(max=30)])
	email = StringField("E-Mail:", validators=[DataRequired(), Email()])
	password = PasswordField("Şifre:", validators=[DataRequired(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message='Şifre 8-30 karakter arasında olmalı ve sadece harf, rakam ve özel karakterler içermelidir.')])
	confirm = PasswordField("Şifreyi Onayla:",validators=[EqualTo('password', message='Şifreler eşleşmiyor!')])
	isAdmin = BooleanField("Kullanıcıyı Admin Yap", default=False)
	submit = SubmitField("Kayıt Ol")

class UpdateProfileForm(FlaskForm):
    name = StringField("Ad:", validators=[DataRequired(), Length(max=50)])
    phone = StringField("Telefon:", validators=[DataRequired(), Length(max=30)])
    email = StringField("E-Mail:", validators=[DataRequired(), Email()])
    password = PasswordField("Yeni Şifre (Değiştirmek istemiyorsanız boş bırakın):", validators=[Optional(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message='Şifre 8-30 karakter arasında olmalı ve sadece harf, rakam ve özel karakterler içermelidir.')])
    confirm = PasswordField("Yeni Şifreyi Onayla:", validators=[EqualTo('password', message='Şifreler eşleşmiyor!')])
    submit = SubmitField("Bilgilerimi Güncelle")

class RequestResetForm(FlaskForm):
    email = StringField('E-Mail:', validators=[DataRequired(), Email()])
    submit = SubmitField('Şifre Sıfırlama Bağlantısı Gönder')

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Yeni Şifre:", validators=[DataRequired(), Regexp(r"^[a-zA-Z0-9_\-&$@#!%^*+.]{8,30}$", message='Şifre 8-30 karakter arasında olmalı ve sadece harf, rakam ve özel karakterler içermelidir.')])
    confirm = PasswordField("Yeni Şifreyi Onayla:", validators=[EqualTo('password', message='Şifreler eşleşmiyor!')])
    submit = SubmitField('Şifremi Sıfırla')
