from recetas import recetas
from utileria import mostrarTodasLasRecetas
from utileria import mostrarRecetas

def borrarRecetas():
    borrarReceta = True
    while borrarReceta:
        mostrarTodasLasRecetas()
        folioBorrar = int(
            input("Ingrese el número de folio de la receta a eliminar: "))

        indexReceta = 0
        indexEncontrado = False
        for receta in recetas:
            if receta[1] == folioBorrar:
                indexEncontrado = True
                break
            else:
                indexReceta += 1

        if indexEncontrado:

            mostrarRecetas(folioBorrar)

            confirmarEliminacionReceta = input(
                "¿Seguro que desea eliminar esta receta? s/n ")

            if confirmarEliminacionReceta.lower() == "s":
                recetas.pop(indexReceta)
                
            print("\nTabla de recetas actualizada:\n")
            mostrarTodasLasRecetas()

            continuar = input("¿Deseas seguir eliminando? s/n ")
            borrarReceta = True if continuar.lower() == "s" else False
        else:
            print("\nEse folio no existe")
            borrarReceta = False
