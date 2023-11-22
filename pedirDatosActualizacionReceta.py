from recetas import recetas
from medicamentos import medicamentos


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
