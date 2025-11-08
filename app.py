from flask import Flask, render_template, request
from flask import make_response, jsonify
import json
import forms

app = Flask(__name__)
 
@app.route('/')
def home():
    return 'Hello, World'

@app.route("/figuras", methods=['GET', 'POST'])
def figuras():
    b = 0
    h = 0
    r = 0
    apotema=0
    res = 0
    figura = ""
    
    figuras_clase = forms.FiguraForm(request.form)

    if request.method == 'POST':
        figura = request.form.get('figura')
        b = float(figuras_clase.base.data or 0)
        h = float(figuras_clase.altura.data or 0)
        r = float(figuras_clase.radio.data or 0)
        apotema = float(figuras_clase.apotema.data or 0)

        if figura == "triangulo":
            res = (b * h) / 2
        if figura == "rectangulo":
            res = b * h
        if figura == "circulo":
            res = 3.1416 * (r ** 2)
        if figura == "pentagono":
            res = (b * apotema) / 2

    return render_template('figuras.html',form=figuras_clase, res=res, figura=figura)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    estudiantes=[]
    datos={}
    tem=[]

    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.email.data
        datos={"matricula":mat,"nombre":nom,"apellido":ape,"correo":em}

        datos_str=request.cookies.get('estudiante')
        if not datos_str:
            return "no hay cookie"
        tem=json.loads(datos_str)
        estudiantes=tem
        print(type(estudiantes))
        estudiantes.append(datos)
        
    response=make_response( render_template('Alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em))

    response.set_cookie('estudiante', json.dumps(estudiantes))

    return response

@app.route("/get_cookie2")
def get_cookie2():
    datos_str=request.cookies.get('estudiante')
    if not datos_str:
        return "No hay cookie"
    datos=json.loads(datos_str)

    return jsonify(datos)
 
@app.route('/index')
def index():
    titulo="IEVN1003 - PWA"
    listado=["Opera 1", "Opera 2", "Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado)
 
@app.route('/operas', methods=['GET', 'POST'])
def operas():
    resultado=0
    if request.method == 'POST':
        x1 = request.form.get('x1')
        x2 = request.form.get('x2')
        resultado=x1+x2
        return render_template('operas.html', resultado=resultado)
    return render_template('operas.html')

 
@app.route('/distancia')
def distancia():
    return render_template('distancia.html')
 
@app.route('/about')
def about():
    return '<h1>This is the about page.</h1>'
 
@app.route('/user/<string:user>')
def user(user):
    return 'Hola ' + user
 
@app.route('/numero/<int:n>')
def numero(n):
    return 'Numero {}'.format(n)
 
@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return 'ID {} nombre: {}'.format(id, username)
 
@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return 'La suma es: {}'.format(n1 + n2)
 
@app.route('/prueba')
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
    '''
 
@app.route("/pizza", methods=['GET', 'POST'])
def pizza():
 
    pizzas = []
    ventas = []
    terminado = False
    total = 0
 
    # Con este se recuperan las cookies 
    pizzas_cookie = request.cookies.get('pizzas')
    if pizzas_cookie:
        pizzas = json.loads(pizzas_cookie)
 
    ventas_cookie = request.cookies.get('ventas')
    if ventas_cookie:
        ventas = json.loads(ventas_cookie)
 
    pizza_form = forms.PizzaForm(request.form)
 
    if request.method == 'POST':
        accion = request.form.get('accion')
 
        # Con esto de aqui se agrega la pizza
        if accion == 'agregar' and pizza_form.validate():
            tamano = pizza_form.tamano.data
            ingredientes = request.form.getlist('ingredientes') 
            cantidad = int(pizza_form.cantidad.data or 0)
 
            precios_tamano = {"chica": 40, "mediana": 80, "grande": 120}
            precio_ingrediente = 10
 
            subtotal = (precios_tamano.get(tamano, 0) + precio_ingrediente * len(ingredientes)) * cantidad
 
            pizza = {
                "tamano": tamano,
                "tamano_display": tamano,
                "ingredientes": ingredientes,
                "ingredientes_display": ', '.join(ingredientes) if ingredientes else 'Ninguno',
                "cantidad": cantidad,
                "subtotal": subtotal
            }
            pizzas.append(pizza)
 
        #quitar pizza
        elif accion == 'quitar_ultimo':
            if pizzas:
                pizzas.pop()
 
        # se termina el pedido aqui
        elif accion == 'terminar':
            nombre = request.form.get('nombre', '')
            direccion = request.form.get('direccion', '')
            telefono = request.form.get('telefono', '')
            if pizzas and nombre:
                total = sum([p["subtotal"] for p in pizzas])
                venta = {
                    "cliente": nombre,
                    "direccion": direccion,
                    "telefono": telefono,
                    "total": total
                }
                ventas.append(venta)
                terminado = True
                pizzas = []  
                #Con esto de arriba es para limpiar el pedido
 
    # Esto es lo del total del dia
    total_dia = sum([v["total"] for v in ventas])
 
    # Esto es para que se muestre (renderice)
    response = make_response(render_template(
        "pizza.html",
        form=pizza_form,
        pizzas=pizzas,
        ventas=ventas,
        terminado=terminado,
        total=total,
        total_dia=total_dia
    ))
 
    # Con esto se guardan las cookies
    response.set_cookie('pizzas', json.dumps(pizzas))
    response.set_cookie('ventas', json.dumps(ventas))
    return response
 
 
@app.route("/get_cookie")
def get_cookie():
    datos_str = request.cookies.get('ventas')
    if not datos_str:
        return "No hay cookie"
    datos = json.loads(datos_str)
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
