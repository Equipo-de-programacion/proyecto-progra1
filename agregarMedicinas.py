from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from medicamentos import medicamentos


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
