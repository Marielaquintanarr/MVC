from modelo.database import db

class DoctorDAO:
    @staticmethod
    def ver(nombre, horario, imagen, rol):
        try:
            response = db.table("doctor").select().execute()
            print(response)
            return True
        except Exception as e:
            print(f"Error al ver: {e}")
            return False
