from pedirDatos import pedirDatos


def agregarPaciente():
    # Pacientes de prueba:
    pacientes = [
        [192, "Alex Nieblas", "Fresnillo 1234","M", 2005, ["Penisilina", "Tierra"]],
        [854, "Adriana Moreno", "Compostela 4321", "F", 1997, []]
    ]

    # Se pide el numero del paciente
    numPaciente = int(input("Ingrese el numero del paciente: "))

    """Variable para saber si algun paciente de la lista ya existe (se hace de 
    esta forma ya que tenemos que iterar sobre la lista y no usar metodos)"""
    existeElPaciente = False

    # Iterar sobre la lista pacientes para ver si el numero de paciente está
    for paciente in pacientes:
        existeElPaciente = True if paciente[0] == numPaciente else False

    """Condicional que en caso de no existir el paciente crear uno e añadirlo a 
    la lista ya hecha y en caso de que si exista decirle que no puede agregar"""
    if existeElPaciente:
        return "No se puede agregar ya que el paciente ya existe"
    else:
        paciente = pedirDatos(numPaciente)
        pacientes.append(paciente)
        return pacientes


pacientes = agregarPaciente()
print(pacientes)
