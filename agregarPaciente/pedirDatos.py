def pedirDatos(numeroDePaciente):
    # Pide la información básica del paciente
    nombrePaciente = input("Ingrese el nombre del paciente: ")
    direccionPaciente = input("Ingrese la dirección del paciente: ")
    sexoPaciente = input("Ingrese el sexo del paciente: M/F ")
    añoPaciente = int(input("Ingrese el año de nacimiento del paciente "))

    # Las alergias se manejan en una lista y en caso de no tener se guardaria la lista vacia
    alergiasPaciente = []
    agregarAlergia = True
    while agregarAlergia == True:
        alergia = input('Ingrese la alergia del paciente: (En caso de no tener no responder) ')
        if len(alergia) <= 0:
            agregarAlergia = False
        else:
            alergiasPaciente.append(alergia)

    # Crea al nuevo paciente y lo retorna
    nuevoPaciente = [numeroDePaciente, nombrePaciente, direccionPaciente, sexoPaciente.upper(), añoPaciente, alergiasPaciente]
    return nuevoPaciente
