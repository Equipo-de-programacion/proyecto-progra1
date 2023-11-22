from recetas import recetas
from pacientes import pacientes
from pandas import pandas

def mostrarTodasLasRecetas():
    folios = []
    fechas = []
    numeros = []
    nombres = []
    direccion = []
    sexos = []
    años = []
    alergias = []

    for receta in recetas:
        pacienteReceta = False
        for paciente in pacientes:
            if paciente[0] == receta[0]:
                pacienteReceta = paciente
        numeros.append(receta[0])
        folios.append(receta[1])
        fechas.append(receta[2])
        nombres.append(pacienteReceta[1])
        direccion.append(pacienteReceta[2])
        sexos.append(pacienteReceta[3])
        años.append(pacienteReceta[4])
        alergias.append(pacienteReceta[5])

    data = {
        "Folio": folios,
        "Fechas": fechas,
        "Numero": numeros,
        "Nombre": nombres,
        "Dirección": direccion,
        "Sexo": sexos,
        "Año de nacimiento": años,
        "Alergias": alergias
        
    }
    print(pandas.DataFrame(data))
