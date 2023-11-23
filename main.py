from pacientes import pacientes
from agregarPaciente import agregarPaciente
from borrarPaciente import borrarPaciente
from actualizarPaciente import actualizarPaciente
from mostrarPacientes import mostrarPacientes
from generarReceta import generarReceta
from borrarRecetas import borrarRecetas
from actualizarRecetaMedica import actualizarRecetaMedica
from mostrarListadoDeMedicamentos import mostrarListadoDeMedicamentos

# Menu
ControladorMenu = 0
# Menu general
while ControladorMenu == 0:
    # Bucle que controla el rango del menu
    while True:
        # No se debe poner un print dentro de un input
        ControladorMenu = int(input(
            "1. Agregar un nuevo paciente al catalogo\n2. Dar de baja un paciente del catalogo\n3. Actualizar los datos de un paciente\n4. Mostrar el listado de pacientes\n5. Generar una receta a un paciente\n6. Eliminar una receta generada\n7. Actualizar los datos de una receta [Presentacion, gramaje y/o dosis]\n8. Mostrar el listado de recetas generadas a determinado paciente \n9. Mostrar listado de medicamentos\n10. Cerrar \nDigite opcion: "))

        if ControladorMenu <= 10 and ControladorMenu >= 1:
            break
        elif ControladorMenu > 10 or ControladorMenu < 1:
            print("Error, digita una opcion valida entre 1 y 10: ")

    # Contacto con los bloques de código
    # SÍ, SÉ QUE SE VE HORRIBLE, PERO ES QUE NO EXISTE EL SWITCH :(
    # Los "HOla[numero]" son para verificar que se ejecute y porque si no me marca error porque no hay instrucciones jajaja"
    if ControladorMenu == 1:
        # llamar funcion 1 y ejecutar segun el problema
        agregarPaciente()
        ControladorMenu = 0
    elif ControladorMenu == 2:
        # llamar funcion 2 y ejecutar segun el problema
        borrarPaciente()
        ControladorMenu = 0
    elif ControladorMenu == 3:
        # llamar funcion 3 y ejecutar segun el problema
        actualizarPaciente()
        ControladorMenu = 0
    elif ControladorMenu == 4:
        # llamar funcion 4 y ejecutar segun el problema
        print(mostrarPacientes(pacientes))
        input()
        ControladorMenu = 0
    elif ControladorMenu == 5:
        # llamar funcion 5 y ejecutar segun el problema
        generarReceta()
        ControladorMenu = 0
    elif ControladorMenu == 6:
        # llamar funcion 6 y ejecutar segun el problema
        borrarRecetas()
        ControladorMenu = 0

    elif ControladorMenu == 7:
        # llamar funcion 7 y ejecutar segun el problema
        actualizarRecetaMedica()
        ControladorMenu = 0
    elif ControladorMenu == 8:
        # llamar funcion 8 y ejecutar segun el problema
        print("Hola8")
    elif ControladorMenu == 9:
        # llamar funcion 9 y ejecutar segun el problema
        mostrarListadoDeMedicamentos()
        input()
        ControladorMenu = 0
    elif ControladorMenu == 10:
        print("Cerrando programa...")
        SystemExit
