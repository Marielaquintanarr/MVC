# app.py
from flask import Flask, request, render_template
from controllers.citaController import insertarCita
from controllers.doctorController import verDoctor
from DAO.verDoctor import DoctorDAO
from DAO.verEnfermero import EnfermeroDAO

app = Flask(__name__)


@app.route('/citas', methods=['GET'])
def formulario():
    return render_template('formularioCita.html')  

@app.route('/doctores', methods=['GET'])
def pagina_doctores():
    doctores = DoctorDAO.ver() 
    return render_template('doctores_info.html', doctores=doctores)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')


@app.route('/enfermeros')
def mostrar_enfermeros():
    enfermeros = EnfermeroDAO.ver()  
    return render_template('enfermeros-info.html', enfermeros=enfermeros)

@app.route('/citas', methods=['POST'])
def agregar_cita():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        
        respuesta = insertarCita(nombre, fecha, hora, motivo, "Pendiente")
        
        if respuesta:
            return render_template('homepage.html')
        else:
            return 'Error al crear cita'

if __name__ == '__main__':
    app.run(debug=True)
