from wtforms import Form
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField
from wtforms import validators
 
class UserForm(Form):
    matricula = IntegerField('Matricula',
    [validators.DataRequired(message="La matricula es obligatoria")])
 
    nombre = StringField('Nombre',
    [validators.DataRequired(message="El campo es requerido")])
 
    apellido = StringField('Apellido',
    [validators.DataRequired(message="El campo es requerido")])
   
    edad = IntegerField('Edad',
    [validators.DataRequired(message="Ingrese Correo Valido")])
 
    email = EmailField('Email',
    [validators.Email(message="Ingrese Correo Valido")])
 
""" ---------------------------------------    FIGURAAS       ---------------------------------------------------------------- """
 
 
class FiguraForm(Form):
 
    base = FloatField('Base')
 
    altura = FloatField('Altura')
 
    radio = FloatField('Radio')
 
    apotema=FloatField('Apotema')
   