from recetas import recetas
from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from tabulate import tabulate

def mostrarRecetasPaciente():
    recetasDelPaciente = []
    print(mostrarPacientes(pacientes))
    numeroPacienteRecetasAMostrar = int(
        input("Ingresa el numero del paciente del que deseas ver las recetas: "))

    for numero in recetas:
        numeroPacienteRecetas = numero[0]
        if numeroPacienteRecetas == numeroPacienteRecetasAMostrar:
            recetasDelPaciente.append(numero)

    print("Listado terminado, mostrando recetas del paciente numero ",
          numeroPacienteRecetasAMostrar)
    print(tabulate(recetasDelPaciente))


mostrarRecetasPaciente()
