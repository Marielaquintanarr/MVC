from modelo.database import db

class DoctorDAO:
    @staticmethod
    def ver():
        try:
            response = db.table("doctor").select("*").execute()
            doctores = response.data 
            return doctores
        except Exception as e:
            print(f"Error al obtener doctores: {e}")
            return []
