#Importamos librerias
import time

#Aqui iniciamos con el diagrama

print("================================================")
print("Bienvenidos a mi Diagrama de como hacer una reservacion de un restaurante en linea")
time.sleep(2)
print("================================================")
print("¿Quieres ir a comer en un restaurante?")
print("1)Si")
print("2)No")
print("================================================")
#Aqui ponemos los checkpoints (No inporta donde se ponga los chackpoints)
checkpoint = False
checkpoint1 = False
checkpoint2 = False
#Aqui iniciamos el bucle con el while true
while True:
#Aqui empezamos a hacer las opciones
    opcion = int(input("Pon aqui tu respuesta"))