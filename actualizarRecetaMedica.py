from mostrarTodasLasRecetas import mostrarTodasLasRecetas
from recetas import recetas
from mostrarPacientes import mostrarPacientes
from pacientes import pacientes
from mostrarRecetas import mostrarRecetas
from pedirDatosActualizacionReceta import pedirDatosActualizacionReceta


def actualizarRecetaMedica():
    actualizarReceta = True
    while actualizarReceta:
        
        mostrarTodasLasRecetas()
        folioActualizar = int(
            input("Ingrese el folio de la receta que desea actualizar: "))

        indexReceta = 0
        indexEncontrado = False
        for receta in recetas:
            if folioActualizar == receta[1]:
                indexEncontrado = True
                break
            else:
                indexReceta += 1

        if not indexEncontrado:
            print("Ese folio no existe")
        else:
            esLaReceta = False
            indexPaciente = 0
            for paciente in pacientes:
                if paciente[0] == recetas[indexReceta][0]:
                    break
                else:
                    indexPaciente += 1

            print(f"\n\n{mostrarPacientes([pacientes[indexPaciente]])}")
            mostrarRecetas(folioActualizar)
            confirmacion = input(f"\n¿Esta es la receta? s/n ")
            esLaReceta = True if confirmacion.lower() == "s" else False

            if esLaReceta:
                nuevaReceta = pedirDatosActualizacionReceta(recetas[indexReceta])
                recetas[indexReceta] = nuevaReceta
                print("\nEsta es la lista de recetas actualizada\n")
                mostrarTodasLasRecetas()
                continuar = input("¿Deseas actualizar otro paciente? s/n ")
                actualizarReceta = True if continuar.lower() == "s" else False

