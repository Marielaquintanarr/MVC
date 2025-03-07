# app.py
from flask import Flask, request, render_template
from controllers.citaController import insertarCita

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/formulario', methods=['GET'])
def formulario():
    return render_template('formularioCita.html')  # Usa la ruta relativa

# Ruta para procesar el formulario cuando se envía
@app.route('/citas', methods=['POST'])
def agregar_cita():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        hora = request.form['hora']
        motivo = request.form['motivo']
        
        # Aquí se llama al controlador que se encarga de insertar los datos
        respuesta = insertarCita(nombre, fecha, hora, motivo, "Pendiente")
        
        if respuesta:
            return f'Se ha creado tu cita {nombre} te esperamos el {fecha} a las {hora}'
        else:
            return 'Error al crear cita'

if __name__ == '__main__':
    app.run(debug=True)
