from clases import Automovil

def solicitar_dato(atributo, tipoDeDato):
    dato = input(atributo)
    dato = dato.strip()
    while not tipoDeDato(dato):
        print("Formato incorrecto, vuelva a ingresar el dato.")
        dato = input(atributo)
    return dato

def validar(dato):
    dato = dato.strip()
    if len(dato) == 0:
        return False
    return True

def crear_automoviles():
    numero = int(solicitar_dato("Número de vehiculos a insertar: ", str.isdigit))
    while numero == 0:
        print("Debe crear al menos un vehículo.")
        numero = int(solicitar_dato("Número de vehiculos a insertar: ", str.isdigit))
        
    vehiculos = {}
    for i in range(numero):
        print(f"Datos del automovil {i+1}:")
        marca = solicitar_dato("Inserte la marca del automovil: ", validar)
        modelo = solicitar_dato("Inserte el modelo: ", validar)
        ruedas = int(solicitar_dato("Inserte el numero de ruedas: ", str.isdigit))
        velocidad = int(solicitar_dato("Inserte la velocidad en km/h: ", str.isdigit))
        cilindraje = int(solicitar_dato("Inserte el cilindraje en cc: ", str.isdigit))
        
        vehiculo = Automovil(marca, modelo, ruedas, velocidad, cilindraje)
        nombre = f"Automovil {i+1}"
        vehiculos[nombre] = vehiculo
        
    print()
    print(f"Se han creado un total de: {i+1} automoviles.")
    return vehiculos

def imprimir_automoviles(diccionario):
    for clave, automovil in diccionario.items():
        print(f"Datos del {clave}\n\nMarca: {automovil.marca}\nModelo: {automovil.modelo}\nNúmero de ruedas: {automovil.nruedas}\nVelocidad: {automovil.velocidad} km/h\nCilindraje: {automovil.cilindraje} cc\n")



automoviles = crear_automoviles()
imprimir_automoviles(automoviles)

