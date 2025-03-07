from modelo.Usuario import Usuario

class Paciente(Usuario):
    def __init__(self, id, nombre, rol):
        super().__init__(id, nombre, rol)
        # {fecha: motivo}
        self.historial_citas = {}
    
    def agendarCita(self):
        pass

    def verEstadoCitas(self):
        pass