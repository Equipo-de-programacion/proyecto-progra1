from pacientes import pacientes


def pedirDatosActualizacion(paciente):
    nombrePaciente = input(
        "Ingrese el nombre del paciente: dejar vacio si no desea actualizar ")
    direccionPaciente = input(
        "Ingrese la dirección del paciente: dejar vacio si no desea actualizar ")
    sexoPaciente = input(
        "Ingrese el sexo del paciente: M/F dejar vacio si no desea actualizar ")
    añoPaciente = input(
        "Ingrese el año de nacimiento del paciente dejar vacio si no desea actualizar ")

    # Las alergias se manejan en una lista y en caso de no tener se guardaria la lista vacia
    alergiasPaciente = []
    agregarAlergia = True
    while agregarAlergia == True:
        alergia = input(
            'Ingrese la alergia del paciente: (En caso de no tener no responder) ')
        if len(alergia) <= 0:
            agregarAlergia = False
        else:
            alergiasPaciente.append(alergia)

    if len(nombrePaciente) <= 0:
        nombrePaciente = paciente[1]
    if len(direccionPaciente) <= 0:
        direccionPaciente = paciente[2]
    if len(sexoPaciente) <= 0:
        sexoPaciente = paciente[3]
    if len(añoPaciente) <= 0:
        añoPaciente = paciente[4]
    else:
        añoPaciente = int(añoPaciente)
    if len(alergiasPaciente) <= 0:
        alergiasPaciente = paciente[5]

    pacienteActualizado = [paciente[0], nombrePaciente,
                           direccionPaciente, sexoPaciente, añoPaciente, alergiasPaciente]
    return pacienteActualizado
