
class Empleado:
    def __init__(self):
        self.VerificarCodigo()
        self.AsignarEstacion()
        self.Nombre = input("Ingrese su nombre: ")
        self.Apellido = input("Ingrese su apellido: ")
        self.AsignarFechaNac()
        self.Password = input("Ingrese su contraseña: ")
    
    #Verificar que el código cumpla con el formato establecido
    def VerificarCodigo (self):
        CodigoAceptado = False
        while CodigoAceptado == False:
            CodigoID = input("Ingrese su codigo ID: ")
            if (CodigoID[0] == "S" or CodigoID[0] == "O") and (CodigoID[1] == "-") and (CodigoID[2:].isdigit):
                self.CodigoID = CodigoID
                CodigoAceptado = True
            else:
                print("Ingrese un código válido.")

    #Asignar las estaciones
    def AsignarEstacion (self):
            if self.CodigoID[0]  == "S":
                self.Estacion = "Supervisor"
            else:
                self.Estacion = input("Ingrese su estacion: ")

    def AsignarFechaNac (self):
        FechaAceptada = False
        while FechaAceptada == False:
            FechaNac = input("Ingrese su fecha de nacimiento: ")
            if len(FechaNac) == 10:
                Dia = int(FechaNac[0:2])
                Espacio1 = [2]
                Mes = int(FechaNac[3:5])
                Espacio2 = [5]
                Año = int(FechaNac[6:10])
                if (Dia > 0 and Dia <= 31) and (Mes > 0 and Mes < 13):
                    self.FechaNac = FechaNac
                    FechaAceptada = True
                else:
                    print("Ingrese una fecha valida.")
            else:
                print("Ingrese una fecha valida.")
        
        


            
  



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
    
    #Historial de produccin
    elif MenuNumero == 4:
        o = 0
        
    #Control de calidad
    elif MenuNumero == 5:
        o = 0
    
    #Pago a operarios
    elif MenuNumero == 6:
        o = 0
    
    #Restablecer contrasena
    elif MenuNumero == 7:
        o = 0

    #Cambiar contrasena
    elif MenuNumero == 8:
        o = 0

    #Salida
    elif MenuNumero == 9:
        print("El programa ha terminado, gracias por preferirnos.")
        Continuar = False

    else:
        print("Ingrese una opcion valida")