#Iniciamos con las librerias
import time
#Iniciamos con la ejecucion del programa
print("================================================")
print("Bienvenidos a programa que te dice si el numero es par o impar")
print("================================================")
#Aqui ponemos lo que se necesita para que el progama haga su magia 
#Aqui se define una variable
num = int(input("Pon aqui el numero que quieres saber si es Par o Impar: "))
#Aqui la variable se divide en 2 y si verifica el resto es 0 es par 
if num % 2 == 0:
    print(f'{num}: Es par :D')
#De lo contrario va a ser impar
else:
    print(f'{num}: Es Impar :0')