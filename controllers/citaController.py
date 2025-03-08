from flask import request, jsonify
from DAO.hacerCita import CitaDAO

from DAO.hacerCita import CitaDAO
from flask import request

def insertarCita(nombre, fecha, hora, motivo, estado):
    # Usamos los datos recibidos en la solicitud
    if CitaDAO.insertar(nombre, fecha, hora, motivo, estado):
        return True
    else:
        return False
