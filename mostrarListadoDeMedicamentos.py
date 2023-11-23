from medicamentos import medicamentos
import pandas


def mostrarListadoDeMedicamentos():
    claves = []
    nombres = []
    presentaciones = []
    gramajes = []
    for medicamento in medicamentos:
        claves.append(medicamento[0])
        nombres.append(medicamento[1])
        presentaciones.append(medicamento[2])
        gramajes.append(medicamento[3])

    datos = {
        "Clave": claves,
        "Nombre": nombres,
        "Presentación": presentaciones,
        "Gramaje/ml": gramajes
    }

    print(f"\n\n{pandas.DataFrame(datos)}\n")
