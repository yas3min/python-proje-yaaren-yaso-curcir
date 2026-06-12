from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FloatField, SelectField
from wtforms.validators import DataRequired

class AddItemForm(FlaskForm):
    name = StringField('Ürün Adı', validators=[DataRequired()])
    price = FloatField('Fiyat', validators=[DataRequired()])
    category = StringField('Kategori', validators=[DataRequired()])
    details = TextAreaField('Detaylar', validators=[DataRequired()])
    image = FileField('Ürün Görseli (İsteğe bağlı)', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Sadece resim dosyaları!')])
    submit = SubmitField('Ürün Ekle')

class EditItemForm(FlaskForm):
    name = StringField('Ürün Adı', validators=[DataRequired()])
    price = FloatField('Fiyat', validators=[DataRequired()])
    category = StringField('Kategori', validators=[DataRequired()])
    details = TextAreaField('Detaylar', validators=[DataRequired()])
    image = FileField('Yeni Ürün Görseli (Değiştirmek istemiyorsanız boş bırakın)', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Sadece resim dosyaları!')])
    submit = SubmitField('Ürünü Güncelle')

class OrderEditForm(FlaskForm):
    status = SelectField('Sipariş Durumu', choices=[('Siparişiniz Alındı', 'Siparişiniz Alındı'), ('Hazırlanıyor', 'Hazırlanıyor'), ('Kargoya Verildi', 'Kargoya Verildi'), ('Teslim Edildi', 'Teslim Edildi')])
    submit = SubmitField('Durumu Güncelle')