from utileria import mostrarPacientes
from pacientes import pacientes
from utileria import pedirDatosActualizacion


def actualizarPaciente():
    actualizarPaciente = True
    while actualizarPaciente:
        if len(pacientes) <= 0:
            print("No hay pacientes para actualizar")
            break
        else:
            print(mostrarPacientes(pacientes))
            pacienteActualizar = int(
                input("Ingrese el paciente que desea actualizar: "))

            indexDelPacienteActualizar = 0
            pacienteEncontrado = False
            # Con este bucle busca el indice en la lista de pacientes en caso de coincidir con alguno
            for paciente in pacientes:
                if paciente[0] == pacienteActualizar:
                    pacienteEncontrado = True 
                    break
                else:
                    indexDelPacienteActualizar += 1
            if not pacienteEncontrado:
                return print("\nEste paciente no existe")
            else:
                print(f"\n{mostrarPacientes([pacientes[indexDelPacienteActualizar]])}")
                pacienteActualizado = pedirDatosActualizacion(pacientes[indexDelPacienteActualizar])
                print(f"\n\n{mostrarPacientes([pacienteActualizado])}")
                confirmación = input("\n¿Esta seguro de los cambios? s/n ")
                if confirmación == "s":
                    pacientes[indexDelPacienteActualizar] = pacienteActualizado
                    print(f"\nLista actualizada: ")
                    print(mostrarPacientes(pacientes))
                    continuar = input("\n¿Desea actualizar otro paciente? s/n ")
                    actualizarPaciente = True if continuar.lower() == "s" else False
