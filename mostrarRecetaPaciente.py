from recetas import recetas
from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from pandas import DataFrame
import tkinter as tk
from tkinter import scrolledtext


def mostrarRecetasPaciente():
    recetasDelPaciente = []
    folios = []
    fechas = []
    indicaciones = []
    medicamentos = []
    print(mostrarPacientes(pacientes))
    numeroPacienteRecetasAMostrar = int(
        input("Ingresa el numero del paciente del que deseas ver las recetas: "))

    for numero in recetas:
        numeroPacienteRecetas = numero[0]
        if numeroPacienteRecetas == numeroPacienteRecetasAMostrar:
            recetasDelPaciente.append(numero)

    print("Listado terminado, mostrando recetas del paciente numero ",
          numeroPacienteRecetasAMostrar)
    for recetaDelPaciente in recetasDelPaciente:
        folios.append(recetaDelPaciente[1])
        fechas.append(recetaDelPaciente[2])
        indicaciones.append(recetaDelPaciente[3])
        medicamentos.append(recetaDelPaciente[4:])
    tabla = DataFrame({
        "Folio": folios,
        "Fechas": fechas,
        "Dosis": indicaciones,
        "Medicamentos": medicamentos
    })
    print(tabla)