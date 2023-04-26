#Aqui ponermo las librerias que vamos a usar :D
import time
#Aqui podemos estilizar un poco el codigo para que no se vea tan feo
print("================================================")
print("Aqui puedes saber si eres mayor de edad\n ¿Quieres averiguarlo?")
#time.sleep(Segundos) es para poner un delay en lo que se va inprimiendo en pantalla
time.sleep(2)
print("1)Si")
print("2)No")
print("================================================")
#time.sleep(Segundos) es para poner un delay en lo que se va inprimiendo en pantalla
time.sleep(2)
#Iniciamos bucle
while True:
#Creamos la variable
    opcion = int(input("Pon aqui tu respuesta: "))
#Aqui ponemos las condiciones de opcion
    if opcion == 1:
        num = int(input("Escribe aqui tu edad: "))
#Aqui ponemos otra variable para que nos guarde la edad ingresada
        if num >= 18:
            print("Felicitaciones eres legal")
            break
#Si no se cumple se ejecuta esta variable
        else:
            print("Lo siento suerte a la proxima")
            break
#Se ejecuta caundo no quiere saber 
    elif opcion == 2:
        break
        print("¿No quieres saber si eres legal?")
#Aqui es cuando ponen un valor no valido
    else:
        print("Esa opcion no esta permitida >:c")