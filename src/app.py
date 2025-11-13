from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            alumno = {'matricula': fila[0], 'nombre': fila[1], 'apaterno': fila[2], 'amaterno': fila[3], 'correo': fila[4]}
            alumnos.append(alumno)
        return jsonify({'alumnos': alumnos, 'mensaje': "Alumnos listados.", "exito":True})
    except Exception as ex:
        return jsonify({'mensaje': "Error" +str(ex), 'exito':False})


def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

def leer_alumno(matricula):
    try:
        cursor = conexion.connection.cursor()
        sql= "Select matricula, nombre, apaterno, amaterno, correo from alumnos where matricula = '{0}'".format(matricula)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            alumno = {'matricula': datos[0], 'nombre': datos[1], 'apaterno': datos[2], 'amaterno': datos[3], 'correo': datos[4]}
            return alumno
        else:
            return None
    except Exception as ex:
        raise ex
@app.route('/alumnos/<matricula>', methods=['GET'])
def leer_curso(matricula):
    try:
        alumno = leer_alumno(matricula)
        if alumno != None:
            return jsonify({'alumno': alumno, 'mensaje': "Alumno encontrado.", 'exito':True})
        else:
            return jsonify({'mensaje': "Alumno no encontrado.", 'exito':False})
    except Exception as ex:
        return jsonify({'mensaje': "Error" +str(ex), 'exito':False})



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()