#Como en los anteriores proyectos Se importan librerias
import time
#Aqui es donde se hace la magia priemro creamos una lista
num = [12, 26, 11, 21, 50]
#Hacemos una variable que inicie en 0 
suma = 0
#Ahora se hace un for y numero va a tomar el valor del elemento actual de num
for numero in num:
#Aqui se toma suma que equivale a 0 y se suma con el numero actual de la lista
    suma += numero
print(suma)