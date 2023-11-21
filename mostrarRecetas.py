from recetas import recetas


def mostrarRecetas(numeroDelPaciente):
    indexOfReceta = 0
    recetaEncontrada = False

    for receta in recetas:
        if receta[0] == numeroDelPaciente:
            recetaEncontrada = True
        else:
            indexOfReceta += 1
    print(indexOfReceta, recetaEncontrada)
