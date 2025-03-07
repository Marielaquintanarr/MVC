from modelo.Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)

    def gestionarHorarios(self):
        pass

    def gestionarCitas(self):
        pass