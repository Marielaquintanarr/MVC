from flask import request, jsonify
from DAO.verDoctor import DoctorDAO
from flask import request

def verDoctor():
    if DoctorDAO.select():
        return True
    else:
        return False
