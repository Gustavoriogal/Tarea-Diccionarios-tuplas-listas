'''Hacer una agenda con un menu:
menu:
1 - Agregar Usuario
2 - Eliminar usuario
3 - Modificar usuario
4 - Mostrar usuario
5 - Mostrar todos los usuarios
6 - Eliminar todos los usuarios

Este seria el menu que debe aparecer y hacer funcionar con todo lo visto hasta ahora, lo
unico que el usuario debe tener por lo menos 4 atributos ej: nombre, apellido, edad,
telefono, dni, direccion, etc.'''
# Definición de la clase Usuario
class Usuario:
    def __init__(self, nombre, apellido, edad, telefono, dni, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.dni = dni
        self.direccion = direccion

# Función para agregar un usuario a la agenda
def agregar_usuario(agenda):
    nombre = input("Ingrese el nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    edad = input("Ingrese la edad del usuario: ")
    telefono = input("Ingrese el teléfono del usuario: ")
    dni = input("Ingrese el DNI del usuario: ")
    direccion = input("Ingrese la dirección del usuario: ")
    
    usuario = Usuario(nombre, apellido, edad, telefono, dni, direccion)
    agenda.append(usuario)
    print("Usuario agregado correctamente.")

# Función para eliminar un usuario de la agenda
def eliminar_usuario(agenda):
    dni = input("Ingrese el DNI del usuario que desea eliminar: ")
    encontrado = False
    
    for usuario in agenda:
        if usuario.dni == dni:
            agenda.remove(usuario)
            encontrado = True
            print("Usuario eliminado correctamente.")
            break  # Se encuentra el usuario y se interrumpe el ciclo
    
    if not encontrado:
        print("No se encontró ningún usuario con ese DNI.")

# Función para modificar un usuario de la agenda
def modificar_usuario(agenda):
    dni = input("Ingrese el DNI del usuario que desea modificar: ")
    encontrado = False
    
    for usuario in agenda:
        if usuario.dni == dni:
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            apellido = input("Ingrese el nuevo apellido del usuario: ")
            edad = input("Ingrese la nueva edad del usuario: ")
            telefono = input("Ingrese el nuevo teléfono del usuario: ")
            direccion = input("Ingrese la nueva dirección del usuario: ")
            
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.edad = edad
            usuario.telefono = telefono
            usuario.direccion = direccion
            
            encontrado = True
            print("Usuario modificado correctamente.")
            break  # Se encuentra el usuario y se interrumpe el ciclo
    
    if not encontrado:
        print("No se encontró ningún usuario con ese DNI.")

# Función para mostrar los datos de un usuario de la agenda
def mostrar_usuario(agenda):
    dni = input("Ingrese el DNI del usuario que desea mostrar: ")
    encontrado = False
    
    for usuario in agenda:
        if usuario.dni == dni:
            print("Nombre:", usuario.nombre)
            print("Apellido:", usuario.apellido)
            print("Edad:", usuario.edad)
            print("Teléfono:", usuario.telefono)
            print("DNI:", usuario.dni)
            print("Dirección:", usuario.direccion)
            
            encontrado = True
            break  # Se encuentra el usuario y se interrumpe el ciclo
    
    if not encontrado:
        print("No se encontró ningún usuario con ese DNI.")

# Función para mostrar todos los usuarios de la agenda
def mostrar_todos(agenda):
    if len(agenda) > 0:
        for usuario in agenda:
            print("Nombre:", usuario.nombre)
            print("Apellido:", usuario.apellido)
            print("Edad:", usuario.edad)
            print("Teléfono:", usuario.telefono)
            print("DNI:", usuario.dni)
            print("Dirección:", usuario.direccion)
            print("-----------")
    else:
        print("No hay usuarios en la agenda.")

# Función para eliminar todos los usuarios de la agenda
def eliminar_todos(agenda):
    agenda.clear()
    print("Todos los usuarios han sido eliminados de la agenda.")

# Función principal para ejecutar el menú
def menu_agenda():
    agenda = []
    
    while True:
        print("MENU:")
        print("1 - Agregar Usuario")
        print("2 - Eliminar Usuario")
        print("3 - Modificar Usuario")
        print("4 - Mostrar Usuario")
        print("5 - Mostrar Todos los Usuarios")
        print("6 - Eliminar Todos los Usuarios")
        print("0 - Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario(agenda)
        elif opcion == "2":
            eliminar_usuario(agenda)
        elif opcion == "3":
            modificar_usuario(agenda)
        elif opcion == "4":
            mostrar_usuario(agenda)
        elif opcion == "5":
            mostrar_todos(agenda)
        elif opcion == "6":
            eliminar_todos(agenda)
        elif opcion == "0":
            break  # Se sale del bucle y finaliza el programa
        else:
            print("Opción inválida. Intente nuevamente.")

# Llamada a la función principal para ejecutar el programa
menu_agenda()
