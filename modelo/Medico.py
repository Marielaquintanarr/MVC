from modelo.Usuario import Usuario

class Medico(Usuario):
    def __init__(self, id, nombre, rol, horario, imagen):
        super().__init__(id, nombre, rol)
        self.horario = horario
        self.imagen = imagen

    def revisarCitas(self):
        pass

    def aceptarCitas(self):
        pass

    def actualizarEstadoConsulta(self):
        pass
