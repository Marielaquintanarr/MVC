from modelo.Usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, id, nombre, rol, imagen, doctor_nombre):
        super().__init__(id, nombre, rol)
        self.imagen = imagen
        self.doctor_nombre = doctor_nombre

    def actualizarEstadoCita(self):
        pass

    def registrarSignosVitales(self):
        pass
    

    