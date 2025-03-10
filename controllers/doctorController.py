from flask import jsonify
from DAO.verDoctor import DoctorDAO

def verDoctor():
    doctores = DoctorDAO.ver()
    if doctores:
        return jsonify(doctores)
    else:
        return jsonify({"error": "No se encontraron doctores"}), 404
