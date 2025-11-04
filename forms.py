from wtforms import Form, StringField, FloatField, EmailField, PasswordField, IntegerField
from wtforms import validators

class UserForm(Form):
   matricula = IntegerField('Matricula', [validators.DataRequired(message="La matricula es obligatoria")])
   nombre = StringField('Nombre', [validators.DataRequired(message="El nombre es obligatorio")])
   apellidos = StringField('Apellidos', [validators.DataRequired(message="Los apellidos son obligatorios")])
   email = EmailField('Email', [validators.DataRequired(message="El email es obligatorio")])
   password = PasswordField('Password', [validators.DataRequired(message="La contraseña es obligatoria")])

class FiguraForm(Form):
 
    base = FloatField('Base')
 
    altura = FloatField('Altura')
 
    radio = FloatField('Radio')
 
    apotema=FloatField('Apotema')


    