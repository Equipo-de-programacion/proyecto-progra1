from recetas import recetas
from pacientes import pacientes
from mostrarPacientes import mostrarPacientes


def mostrarRecetasPaciente():
    recetasDelPaciente = list()
    print(mostrarPacientes(pacientes))
    numeroPacienteRecetasAMostrar = int(
        input("Ingresa el numero del paciente del que deseas ver las recetas: "))

    for numero in pacientes:
        numeroPacienteRecetas = (recetas[0])
        if numeroPacienteRecetas == numeroPacienteRecetasAMostrar:
            recetasDelPaciente.append(recetas[numero])

    print("Listado terminado, mostrando recetas del paciente numero ",
          numeroPacienteRecetasAMostrar)
    print(recetasDelPaciente)

