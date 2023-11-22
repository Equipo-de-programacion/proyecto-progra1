from recetas import recetas

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
