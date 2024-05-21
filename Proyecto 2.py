
class Empleado:
    def __init__(self):
        CodigoID = input("Ingrese su codigo ID: ")
        Estacion = input("Ingrese su estacion: ")
        Nombre = input("Ingrese su nombre: ")
        Apellido = input("Ingrese su apellido: ")
        FechaNac = input("Ingrese su fecha de nacimiento: ")
        Password= input("Ingrese su contraseña: ")
        self.CodigoID = CodigoID
        self.Estacion = Estacion
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNac = FechaNac
        self.Password = Password

SuperVisor = Empleado()



Continuar = True
while Continuar == True:
    #Menu
    print("Bienvenido a Laboratorio Dolorín")
    print("1. Ingresar operarios")
    print("2. Mostrar equipo de trabajo")
    print("3. Simular paso del tiempo")
    print("4. Historial de producción")
    print("5. Control de calidad")
    print("6. Pago a operarios")
    print("7. Restablecer contraseña")
    print("8. Cambiar contraseña")
    print("9. Salida")
    MenuNumero = int(input("ingrese la opcion deseada: "))

    #Ingresar operarios
    if MenuNumero == 1:
        o = 0

    #Mostrar equipo de trabajo
    elif MenuNumero == 2:
        o = 0

    #Simular paso del tiempo
    elif  MenuNumero == 3:
        o = 0
    
    #Historial de producción
    elif MenuNumero == 4:
        o = 0
        
    #Control de calidad
    elif MenuNumero == 5:
        o = 0
    
    #Pago a operarios
    elif MenuNumero == 6:
        o = 0
    
    #Restablecer contraseña
    elif MenuNumero == 7:
        o = 0

    #Cambiar contraseña
    elif MenuNumero == 8:
        o = 0

    #Salida
    elif MenuNumero == 9:
        print("El programa ha terminado, gracias por preferirnos.")
        Continuar = False

    else:
        print("Ingrese una opcion valida")