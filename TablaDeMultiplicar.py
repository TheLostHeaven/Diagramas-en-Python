#Aqui importamos las librerias necesarias
import time
print("============================================================")
#Aqui abrimos un bucle para que el programa este en constante ejecucion y si uno pone un valor Invalido se siga ejecutando
while True:
    try:
        #Aqui es para que el usuario pueda ingresar el numero
        num = int(input("Ingresa un número para generar su tabla de multiplicar: "))
        break
    #aqui es para que salga una advertencia cuando el usuario poner valores no permitidos
    except ValueError:
        print("Por favor, Inserta un numero valido")
print("============================================================")

#Aqui va la logica para que haga las tablas de multiplicar y que lo imprima
for i in range(1, 11):
    resultado = num * i
    time.sleep(.5)
    print(f"{num} x {i} = {resultado}")