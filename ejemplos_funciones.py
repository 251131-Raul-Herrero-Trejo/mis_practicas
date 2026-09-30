import datetime

def saludar():
    print("Hola, Bienvenid@s")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es: {resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")
saludar_persona("Raul",19)    

# Ejemplos funciones con parametros

def sumar_numeros(numero1, numero2):
    resultado_suma=numero1+numero2
    print(f"El resultado de la suma es: {resultado_suma}")
sumar_numeros(5,5)

def calcular_iva(valor_inicial):
    iva=valor_inicial*0.16
    total=valor_inicial+iva
    print(f"El total del valor con iva incluido es: {total}")
calcular_iva(200)

# Ejemplos funciones sin parametros

def mostrar_menu():
    print("=== MENU PRINCIPAL ===")
    print("1 Ver perfil")
    print("2 Configuración")
    print("3 Cerrar sesion")
    print("======================")
mostrar_menu()    

def mostrar_anio_actual():
    hoy = datetime.datetime.now()
    print(f"El año actual es: {hoy.year}")
mostrar_anio_actual()
