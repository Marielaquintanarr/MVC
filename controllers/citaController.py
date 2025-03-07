from flask import request, jsonify
from DAO.hacerCita import CitaDAO

# def insertarCita():
#     data = request.json
#     if CitaDAO.insertar(data['nombre'], data['fecha'], data['hora'], data['motivo'], data['estado']):
#         return jsonify({"mensaje": "Cita creada correctamente"}), 201
#     else:
#         return jsonify({"mensaje": "Error al crear cita"}), 400

# controllers/citaController.py
from DAO.hacerCita import CitaDAO
from flask import request

def insertarCita(nombre, fecha, hora, motivo, estado):
    # Usamos los datos recibidos en la solicitud
    if CitaDAO.insertar(nombre, fecha, hora, motivo, estado):
        return True
    else:
        return False
