from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from medicamentos import medicamentos
from recetas import recetas
import pandas


def agregarMedicinas(indexPaciente, folio, fecha):
    medicinasParaElPaciente = []
    medicina = True
    while medicina:
        print(f"\n{mostrarPacientes([pacientes[indexPaciente]])}")

        # Medicina
        medicinaCodigo = input("¿Cual es el código de la medicina?: ")
        indexMedicina = 0
        medicinaEncontrada = False
        medicinaActual = False
        for medicina in medicamentos:
            if medicina[0] == medicinaCodigo:
                medicinaEncontrada = True
                medicinaActual = medicina
                break
            else:
                indexMedicina += 1

        if medicinaEncontrada:
            medicinasParaElPaciente.append(medicinaActual)
            print("Medicina agregada\n")
            continuarAgregando = input("¿Desea agregar otra medicina a la receta? s/n ")
            medicina = True if continuarAgregando.lower() == "s" else False
        else:
            return print("Esa medicina no existe ")

    print(f"Folio: {folio}")
    print(f"Fecha: {fecha}\n")
    for medicinaParaElPaciente in medicinasParaElPaciente:
        print(f"Código: {medicinaParaElPaciente[0]}")
        print(f"Nombre cientifico: {medicinaParaElPaciente[1]}")
        print(f"Presentación: {medicinaParaElPaciente[2]}")
        print(f"Gramaje/ml: {medicinaParaElPaciente[3]}\n")
    
    return medicinasParaElPaciente

def confirmarPaciente(paciente):
    alergias = "Ninguna" if len(paciente[5]) <= 0 else paciente[5]
    print(
        f"\nNombre: {paciente[1]}\nDirección: {paciente[2]}\nSexo: {paciente[3]}\nAño de nacimiento: {paciente[4]}\nAlergias: {alergias}")
    respuesta = input("\n\n¿Confirmar el registro?: s/n ")
    return respuesta.lower() == "s"

def mostrarRecetas(folioReceta):
    indexOfReceta = 0
    recetaEncontrada = False
    recetasCompletas = []

    for receta in recetas:
        if receta[1] == folioReceta:
            recetaEncontrada = True
            recetasCompletas.append(receta)
            indexOfReceta += 1
        else:
            indexOfReceta += 1

    if recetaEncontrada:
        for receta in recetasCompletas:
            print(f"\nFolio: {receta[1]}\nFecha: {receta[2]}\n")

            for medicamentos in range(4, len(receta)):
                print(f"Código: {receta[medicamentos][0]}")
                print(f"Nombre cienífico: {receta[medicamentos][1]}")
                print(f"Presentacion: {receta[medicamentos][2]}")
                print(f"Grmaje/ml: {receta[medicamentos][3]}\n")

            print(receta[3])

def mostrarPacientes(listaPacientes):
    if len(listaPacientes) <= 0:
        return "Por el momento no hay paciente"
    else:
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

def mostrarRecetasPaciente():
    recetasDelPaciente = list()
    print(mostrarPacientes(pacientes))
    numeroPacienteRecetasAMostrar = int(
        input("Ingresa el numero del paciente del que deseas ver las recetas: "))

    for numero in pacientes:
        numeroPacienteRecetas = (recetas[0])
        if numeroPacienteRecetas == numeroPacienteRecetasAMostrar:
            recetasDelPaciente.append(recetas[numero])

    print("Listado terminado, mostrando recetas del paciente numero ",
          numeroPacienteRecetasAMostrar)
    print(recetasDelPaciente)

def mostrarTodasLasRecetas():
    folios = []
    fechas = []
    numeros = []
    nombres = []
    direccion = []
    sexos = []
    años = []
    alergias = []

    for receta in recetas:
        pacienteReceta = False
        for paciente in pacientes:
            if paciente[0] == receta[0]:
                pacienteReceta = paciente
        numeros.append(receta[0])
        folios.append(receta[1])
        fechas.append(receta[2])
        nombres.append(pacienteReceta[1])
        direccion.append(pacienteReceta[2])
        sexos.append(pacienteReceta[3])
        años.append(pacienteReceta[4])
        alergias.append(pacienteReceta[5])

    data = {
        "Folio": folios,
        "Fechas": fechas,
        "Numero": numeros,
        "Nombre": nombres,
        "Dirección": direccion,
        "Sexo": sexos,
        "Año de nacimiento": años,
        "Alergias": alergias
        
    }
    print(pandas.DataFrame(data))

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

def pedirDatosActualizacionReceta(receta):

    nuevosMedicamentos = []
    fecha = False

    nuevaFecha = input("Ingresa la nueva fecha: ")
    if len(nuevaFecha) > 0:
        fecha = nuevaFecha
    else:
        fecha = receta[2]

    for recetaIndividual in range(4, len(receta)):
        nuevoCodigo = input(
            f"Cambia el codigo de la receta {receta[recetaIndividual][0]} -> ")
        if len(nuevoCodigo) > 0:
            # Validar codigo:
            codigoValido = False
            for medicamento in medicamentos:
                if medicamento[0] == nuevoCodigo:
                    nuevoMedicamento = list(medicamento)
                    nuevosMedicamentos.append(nuevoMedicamento)
                    codigoValido = True
                    break
            if codigoValido:
                print("Codigo valido")
            else:
                print("El codigo no existe asi que no se actualizará")
                nuevosMedicamentos.append(medicamento)
        else:
            nuevosMedicamentos.append(receta[recetaIndividual])

    dosis = False
    nuevaDosis = input(
        "Ingrese la dosis de la receta en caso de querer cambiarla: ")

    dosis = nuevaDosis if len(nuevaDosis) > 0 else receta[3]
    recetaActualizada = [receta[0], receta[1],
                         fecha, dosis, nuevosMedicamentos]
    return recetaActualizada

