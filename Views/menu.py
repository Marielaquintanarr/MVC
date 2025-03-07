from controllers.citaController import CitaDAO

def menu():
    controller = CitaDAO()
    nombre = input('Nombre del paciente: ')
    fecha = input('Fecha de la cita (dd/mm/aaaa): ')
    hora = input('Ingrese la hora (16:00PM): ')
    motivo = input('Motivo de consulta: ')

    respuesta = controller.insertar(nombre, fecha, hora, motivo, "Pendiente")
    if respuesta:
        print("Cita creada")
    else:
        print("Error al crear cita")

menu()
