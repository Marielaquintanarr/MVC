from flask import request, jsonify
from DAO.hacerCita import CitaDAO

from DAO.hacerCita import CitaDAO
from flask import request

from modelo.Cita import Cita

def insertarCita(nombre, fecha, hora, motivo, estado):
    # Usamos los datos recibidos en la solicitud
    cita = Cita(nombre, fecha, hora, motivo, estado)
    if CitaDAO.insertar(cita):
        return True
    else:
        return False

def verCitas():
    citas = CitaDAO.verCitas()
    if citas:
        return citas
    else:
        return [{"error": "No se encontraron citas"}]