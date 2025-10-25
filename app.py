from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route('/index')
def index():
    titulo="IEVN1003 - Programación Web"
    listado=["Opera 1", "Opera 2", "Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/operas', methods=['GET', 'POST'])
def operas():
    if request.method == 'POST':
        x1 = request.form.get('n1', type=float)
        x2 = request.form.get('n2', type=float)
        resultado = x1 + x2
        return render_template('operas.html', resultado=resultado)
    return render_template('operas.html')


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')



@app.route('/about')
def about():
    return "This is the about page"

@app.route('/user/<string:user>')
def user(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "Id: {} Name: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route("/prueba")
def prueba():
    return '''
    <h1> Prueba HTML </h1>
    <p> Este es un parrafo </p>
    <ul>
        <li> Cosa 1 </li>
        <li> Cosa 2 </li>
        <li> Cosa 3 </li>
    </ul>
    '''



if __name__ == "__main__":
    app.run(debug=True)