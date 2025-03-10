from modelo.database import db

class EnfermeroDAO:
    @staticmethod
    def ver():
        try:
            response = (
                db.from_("enfermero")
                .select("nombre, rol, imagen, doctor(nombre)")
                .execute()
            )

            enfermeros = response.data  
            print("Datos obtenidos:", enfermeros)  # Para verificar la respuesta
            return enfermeros
        except Exception as e:
            print(f"Error al obtener enfermeros: {e}")
            return []
