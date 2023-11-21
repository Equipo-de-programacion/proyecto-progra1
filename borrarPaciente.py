from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from mostrarRecetas import mostrarRecetas


def borrarPaciente():
    print(mostrarPacientes(pacientes))

    pacienteAEliminar = int(input("Ingrese el numero del paciente a eliminar: "))

    indexDelPacienteAEliminar = 0
    pacienteEncontrado = False

    for paciente in pacientes:
        if paciente[0] == pacienteAEliminar:
            pacienteEncontrado = True
            break
        else:
            indexDelPacienteAEliminar += 1

    if not pacienteEncontrado:
        print("Este paciente no existe")
    else:
        print(f"\n{mostrarPacientes([pacientes[indexDelPacienteAEliminar]])}")
        mostrarRecetas(indexDelPacienteAEliminar)
