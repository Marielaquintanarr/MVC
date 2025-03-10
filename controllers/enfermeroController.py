from flask import jsonify
from DAO.verEnfermero import EnfermeroDAO

def verEnfermeri():
    enfermeros = EnfermeroDAO.ver()
    if enfermeros:
        return jsonify(enfermeros)
    else:
        return jsonify({"error": "No se encontraron enfermeros"}), 404
