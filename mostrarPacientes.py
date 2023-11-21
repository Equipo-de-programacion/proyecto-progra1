# Esta funcion utiliza pandas para crear la tabla y pandas necesita un diccionario
# con una clave y el valor en forma de array asi que a esta funcion se le pasa como
# argumento la lista de pacientes para poder separarla e imprimirla con formato
import pandas

def mostrarPacientes(listaPacientes):
    numerosPacientes = []
    nombresPacientes = []
    direccionPacientes = []
    sexoPacientes = []
    añoPacientes = []
    alergiasPacientes = []
    for paciente in listaPacientes:
        numerosPacientes.append(paciente[0])
        nombresPacientes.append(paciente[1])
        direccionPacientes.append(paciente[2])
        sexoPacientes.append(paciente[3])
        añoPacientes.append(paciente[4])
        if len(paciente[5]) <= 0:
            alergiasPacientes.append("Ninguna")
        else:
            alergiasPacientes.append(paciente[5])

    data = {
        "Numero": numerosPacientes,
        "Nombre": nombresPacientes,
        "Direccion": direccionPacientes,
        "Sexo": sexoPacientes,
        "Año": añoPacientes,
        "Alergias": alergiasPacientes
    }

    return pandas.DataFrame(data)
