#Librerias Utilizadas
import random
#Variables globales
ArregloEmpleados = []
EstacionUno = []
EstacionDos = []
EstacionTres = []
Estaciones = []
TiempoSimulado = False
#Clase Empleado
class Empleado:
    def __init__(self):
        self.VerificarCodigo()
        self.AsignarEstacion()
        self.Nombre = input("Ingrese su nombre: ") #Se le asigna valor al atributo
        self.Apellido = input("Ingrese su apellido: ") #Se le asigna valor al atributo
        self.AsignarFechaNac()
        self.Password = input("Ingrese su contraseña: ") #Se le asigna valor al atributo
    
    #Verificar que el código cumpla con el formato establecido
    def VerificarCodigo (self):
        CodigoAceptado = False
        while CodigoAceptado == False:
            CodigoExiste = False
            CodigoID = input("Ingrese su codigo ID: ")
            for Empleado in ArregloEmpleados:
                if Empleado.CodigoID == CodigoID:
                    CodigoExiste = True
                    print("El codigo ya existe")
            if (CodigoID[0] == "S" or CodigoID[0] == "O") and (CodigoID[1] == "-") and (CodigoID[2:].isdigit) and (CodigoExiste == False):
                if len(ArregloEmpleados) == 0 and CodigoID[0] == "S":
                    self.CodigoID = CodigoID #Se le asigna valor al atributo
                    CodigoAceptado = True
                elif len(ArregloEmpleados) >= 1 and CodigoID[0] == "O":
                    self.CodigoID = CodigoID #Se le asigna valor al atributo
                    CodigoAceptado = True
                else: 
                    print("Primero se deben de ingresar los datos del supervisor de planta.")
                    print("Debe haber solo un supervisor en la planta.")
            else:
                print("Ingrese un codigo valido.")

    #Asignar las estaciones
    def AsignarEstacion (self):
            if (self.CodigoID[0]  == "S") or (len(ArregloEmpleados)==0):
                self.Estacion = "Supervisor" #Se le asigna valor al atributo
            else:
                self.Estacion = input("Ingrese su estacion: ") #Se le asigna valor al atributo

    def AsignarFechaNac (self):
        FechaAceptada = False
        while FechaAceptada == False:
            FechaNac = input("Ingrese su fecha de nacimiento:   (DD-MM-YYYY) ")
            if len(FechaNac) == 10:
                Dia = int(FechaNac[0:2])
                Mes = int(FechaNac[3:5])
                Año = int(FechaNac[6:10])
                if (Dia > 0 and Dia <= 31) and (Mes > 0 and Mes < 13) and (FechaNac[2] == "-" and FechaNac[5] == "-"):
                    self.FechaNac = FechaNac #Se le asigna valor al atributo
                    FechaAceptada = True
                else:
                    print("Ingrese una fecha valida.")
                
            else:
                print("Ingrese una fecha valida.")

#Funciones del Laboratorio  
def HistorialDeProduccion():
    for i,Estacion in enumerate(Estaciones,start=1):
        Texto= "Estacion"+str(i)
        for Dia in Estacion:
             Texto = Texto + '\t' + str(Dia)
        print (Texto)

def CalculoSalarios():
    for i,Estacion in enumerate (Estaciones,start=1):
        Texto = "Estacion"+str(i)
        for Dia in Estacion:
            if Dia >= 100:
                Paga = (Dia * 5) + 15
            else:
                Paga = Dia * 5
            Texto = Texto + '\t' + "$" + str(Paga)
        print(Texto)

def RestaurarPassword(CodigoID):
    EmpleadoEncontrado = False
    for Empleado in ArregloEmpleados:
        if Empleado.CodigoID == CodigoID:
            Empleado.Password = Empleado.Nombre + "." + Empleado.Apellido + Empleado.FechaNac[6:10]
            print("La contrasena ha sido restaurada.")
            EmpleadoEncontrado = True
            break
    if EmpleadoEncontrado == False:
        print("No se encontro el empleado")
        
def CambiarPassword(CodigoID, PasswordActual, PasswordNuevo):
    EmpleadoEncontrado = False
    for Empleado in ArregloEmpleados:
        if Empleado.CodigoID == CodigoID:
            if Empleado.Password == PasswordActual:
                Empleado.Password = PasswordNuevo
                print("La contrasena ha sido cambiada.")
                EmpleadoEncontrado = True
                break
            else:
                print("Las contrasenas no coinciden.")
    if EmpleadoEncontrado == False:
        print("No se encontro el empleado")

        
#Inicio del programa        
print("Bienvenido a Laboratorio Dolorin")
print("Ingrese los datos del supervisor de planta")
#Creando al empleado Supervisor
Supervisor = Empleado()
#Agregando al supervisor al listado de colaboradores
ArregloEmpleados.append (Supervisor)


Continuar = True
while Continuar == True:
    #Menu
    print("1. Ingresar operarios")
    print("2. Mostrar equipo de trabajo")
    print("3. Simular paso del tiempo")
    print("4. Historial de produccion")
    print("5. Control de calidad")
    print("6. Pago a operarios")
    print("7. Restablecer contrasena")
    print("8. Cambiar contrasena")
    print("9. Salida")
    MenuNumero = int(input("ingrese la opcion deseada: "))

    #Ingresar operarios
    if MenuNumero == 1:
        #Ciclo de registro operadores
        for i in range(0,3):
            print(f"Ingresar información del empleado {i+1}:" )
            Operador = Empleado()
            ArregloEmpleados.append(Operador)

    #Mostrar equipo de trabajo
    elif MenuNumero == 2:
        Encabezados = 'CodigoID\tEstacion\tNombre\tApellido\tFechaNac.\tContrasena'
        print(Encabezados)
        for Operador in ArregloEmpleados:
            Texto = Operador.CodigoID + '\t' + Operador.Estacion + '\t' + Operador.Nombre + '\t' + Operador.Apellido + '\t' + Operador.FechaNac + '\t' + Operador.Password
            print(Texto)

    #Simular paso del tiempo
    elif  MenuNumero == 3:
        #Limpiar los arreglos para almacenar solo una semana
        EstacionUno.clear()
        EstacionDos.clear()
        EstacionTres.clear()
        Estaciones.clear()
        #Generar produccion de estaciones de trabajo
        for i in range(0,5):
            EstacionUno.append(random.randint(75,120)) #Fuente: W3Schools
            EstacionDos.append(random.randint(75,120))
            EstacionTres.append(random.randint(75,120))
        #Agregar una copia de los arreglos para conservar los valores aleatorios generados originalmente
        Estaciones.append(EstacionUno.copy())
        Estaciones.append(EstacionDos.copy())
        Estaciones.append(EstacionTres.copy())
        TiempoSimulado = True
        print("Simulacion de tiempo completada")
            
    #Historial de produccion
    elif MenuNumero == 4:
        if TiempoSimulado == False:
            print("Para ingresar a esta función, primero simule el paso del tiempo.")
        else:
            HistorialDeProduccion()
        
    #Control de calidad
    elif MenuNumero == 5:
        if TiempoSimulado == False:
            print("Para ingresar a esta función, primero simule el paso del tiempo.")
        else:
            print("Valores de produccion antes de control de calidad")
            HistorialDeProduccion()
            for i,Dia in enumerate(Estaciones[0],start=0):
                Estaciones[0][i] = round(Dia*0.9) 
            for i,Dia in enumerate(Estaciones[1],start=0):
                Estaciones[1][i] = round(Dia*0.94)
            for i,Dia in enumerate(Estaciones[2],start=0):
                Estaciones[2][i] = round(Dia*0.97)
            print("Valores de produccion despues de control de calidad")
            HistorialDeProduccion()
    
    #Pago a operarios
    elif MenuNumero == 6:
        if (TiempoSimulado == False):
            print("Para ingresar a esta función, primero simule el paso del tiempo.")
        else:
            CalculoSalarios()

    #Restablecer contrasena
    elif MenuNumero == 7:
        CodigoID = input("Ingrese el codigo ID del operario a cambiar contraseña: ")
        RestaurarPassword(CodigoID)

    #Cambiar contrasena
    elif MenuNumero == 8:
        CodigoID = input("Ingrese el codigo ID del operario a cambiar contraseña: ")
        PasswordActual = input("Ingrese el password actual: ")
        PasswordNuevo = input("Ingrese el password nuevo: ")
        CambiarPassword(CodigoID,PasswordActual,PasswordNuevo)

    #Salida
    elif MenuNumero == 9:
        print("El programa ha terminado, gracias por preferirnos.")
        Continuar = False

    else:
        print("Ingrese una opcion valida")