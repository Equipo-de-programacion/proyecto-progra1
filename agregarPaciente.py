"""La funcion llama a otra una vez valida que ese numero de paciente no existe
y al final retorna la lista con ese nuevo paciente"""

from pedirDatos import pedirDatos
from pacientes import pacientes
from mostrarPacientes import mostrarPacientes
from confirmarPaciente import confirmarPaciente

def agregarPaciente():
    agregarPaciente = True
    while (agregarPaciente):
        # Se pide el numero del paciente
        numPaciente = int(input("Ingrese el numero del paciente: "))

        """Variable para saber si algun paciente de la lista ya existe (se hace de 
      esta forma ya que tenemos que iterar sobre la lista y no usar metodos)"""
        existeElPaciente = False

        # Iterar sobre la lista pacientes para ver si el numero de paciente está
        for paciente in pacientes:
            existeElPaciente = True if paciente[0] == numPaciente else False

        """Condicional que en caso de no existir el paciente crear uno e añadirlo a 
      la lista ya hecha y en caso de que si exista decirle que no puede agregar"""
        if existeElPaciente:
            print("No se puede agregar ya que el paciente ya existe")
            break
        else:
            paciente = pedirDatos(numPaciente)
            respuesta = confirmarPaciente(paciente)
            if respuesta:
                pacientes.append(paciente)
                print(f"\n{mostrarPacientes(pacientes)}\n")
                deseaContinuar = input("¿Desea agregar otro paciente?: s/n ")
                agregarPaciente = False if deseaContinuar.lower() == "n" else True
