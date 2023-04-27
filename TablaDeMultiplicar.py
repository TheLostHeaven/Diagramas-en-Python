#Importamos librerias :D
import time
print("============================================================")
num = int(input("Ingresa un número para generar su tabla de multiplicar: "))
print("============================================================")
for i in range(1, 11):
    resultado = num * i
    time.sleep(.5)
    print(f"{num} x {i} = {resultado}")