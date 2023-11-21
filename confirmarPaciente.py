#Esta función lo que hace es mostrar el paciente que quiere crear y preguntarle
#si está de acuerdo con los datos y retorna un boolean dependiendo su respuesta

def confirmarPaciente(paciente):
    alergias = "Ninguna" if len(paciente[5]) <= 0 else paciente[5]
    print(
        f"\nNombre: {paciente[1]}\nDirección: {paciente[2]}\nSexo: {paciente[3]}\nAño de nacimiento: {paciente[4]}\nAlergias: {alergias}")
    respuesta = input("\n\n¿Confirmar el registro?: s/n ")
    return respuesta.lower() == "s"
