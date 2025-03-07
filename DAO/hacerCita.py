from modelo.database import db

class CitaDAO:
    @staticmethod
    def insertar(nombre, fecha, hora, motivo, estado):
        data = {
            'nombre': nombre,
            'fecha': fecha,
            'hora': hora,
            'motivo': motivo,
            'estado': estado
        }

        try:
            response = db.table("cita").insert(data).execute()
            print(response)
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
