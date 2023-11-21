# Este modulo elimina al paciente que indique el medico primero pide el numero de paciente y lo busca en la lista de pacientes
# En caso de encontrarlo muestra al paciente y sus recetas en caso de tener y pide confirmacion

from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from mostrarRecetas import mostrarRecetas
from recetas import recetas


def borrarPaciente():
    eliminarPaciente = True
    while (eliminarPaciente):
        if len(pacientes) <= 0:
            print("No hay pacientes el la lista")
            break
        else:
            # Muestra los pacientes actuales
            print(mostrarPacientes(pacientes))

            # Pide el numero de paciente que desea eliminar
            pacienteAEliminar = int(
                input("Ingrese el numero del paciente a eliminar: "))

            indexDelPacienteAEliminar = 0
            pacienteEncontrado = False
            # Con este bucle busca el indice en la lista de pacientes en caso de coincidir con alguno
            for paciente in pacientes:
                if paciente[0] == pacienteAEliminar:
                    pacienteEncontrado = True
                    break
                else:
                    indexDelPacienteAEliminar += 1

            if not pacienteEncontrado:
                print("Este paciente no existe")
            else:
                print(
                    f"\n{mostrarPacientes([pacientes[indexDelPacienteAEliminar]])}\n")
                print("RECETAS")
                mostrarRecetas(pacienteAEliminar)
                confirmarAccion = input(
                    "Realmente desea eliminar al paciente y todas sus recetas s/n ")

                if confirmarAccion.lower() == "s":
                    pacientes.pop(indexDelPacienteAEliminar)

                    for receta in recetas:
                        if receta[0] == pacienteAEliminar:
                            recetas.remove(receta)

            print(f"\n{mostrarPacientes(pacientes)}")
            seguirBorrando = input("¿Continuar con otro paciente? s/n ")
            eliminarPaciente = True if seguirBorrando.lower() == "s" else False


borrarPaciente()
