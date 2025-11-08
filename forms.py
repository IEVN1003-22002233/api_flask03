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
    

class PizzaForm(Form):
    nombre = StringField('Nombre', [validators.DataRequired()])
    direccion = StringField('Dirección', [validators.DataRequired()])
    telefono = StringField('Teléfono', [validators.DataRequired()])
    fecha = StringField('Fecha (dd-mm-aaaa)', [validators.DataRequired()])

    tamano = StringField('Tamaño (chica / mediana / grande)', [validators.DataRequired()])
    ingredientes = StringField('Ingredientes', [validators.DataRequired()])
    cantidad = IntegerField('Cantidad', [validators.DataRequired()])