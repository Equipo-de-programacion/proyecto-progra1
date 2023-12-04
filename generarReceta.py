from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from utileria import agregarMedicinas
from recetas import recetas
import random


def generarReceta():
    crearReceta = True
    folio = random.randrange(1, 10000)
    receta = False

    while (crearReceta):
        print(f"\n{mostrarPacientes(pacientes)}")
        pacienteReceta = int(
            input("¿A que paciente quieres hacer la receta? "))

        indexDelPacienteReceta = 0
        pacienteEncontrado = False
        # Con este bucle busca el indice en la lista de pacientes en caso de coincidir con alguno
        for paciente in pacientes:
            if paciente[0] == pacienteReceta:
                pacienteEncontrado = True
                break
            else:
                indexDelPacienteReceta += 1

        if not pacienteEncontrado:
            print("Este paciente no existe")
            crearReceta = False
        else:
            fecha = input(
                "Ingrese la fecha en el siguiente formato: DD/MM/YYY ")
            medicinasParaElPaciente = agregarMedicinas(
                indexDelPacienteReceta, folio, fecha, pacienteReceta)

            if type(medicinasParaElPaciente) == list:
                Dosis = input("¿Cual es la dosis de esta receta?: ")
                confirmacion = input("\n¿Quieres confirmar esta receta? s/n ")

                if confirmacion.lower() == "s":
                    receta = [pacienteReceta, folio, fecha, Dosis]
                    for medicinaParaElPaciente in medicinasParaElPaciente:
                        receta.append(medicinaParaElPaciente)

                    continuar = input("¿Desea generar otra receta? s/n ")
                    crearReceta = True if continuar.lower() == "s" else False
    recetas.append(receta)
