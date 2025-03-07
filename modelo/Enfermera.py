from modelo.Usuario import Usuario

class Enfermera(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)

    def actualizarEstadoCita(self):
        pass

    def registrarSignosVitales(self):
        pass
    

    