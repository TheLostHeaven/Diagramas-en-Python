#Importamos las librerias 
import time
#Aqui empezamos a hacer el codigo 
#Primera mente hacemos de que es el programa e imprimimos lo que hacer
print("==================================================================================")
print("Bienvenidos a mi Diagrama de como hacer una reservacion de un restaurante en linea")
print("==================================================================================")
time.sleep(2)
print("¿Quieres ir a comer en un restaurante?")
print("1)Si")
print("2)No")
print("================================================")
#Aqui empezamos a dar funcionalidad al programa
opcion = 0
while True:
#Creamos una opcion 
    opcion = int(input("Pon aqui tu opcion: "))
    print("================================================")
    time.sleep(2)
    if opcion == 1:
        print("Listo, entra a tu telefono o computadora y busca en Google\nEntra a la pagina de preferencia")
        print("¿Encotraste disponibilidad para las 8?")
        print("1)Si")
        print("2)No")
        print("================================================")
#aqui inciamos la seguna opciony es la opcion anidadas
        opcion2 = int(input("Pon tu opcion aqui: "))
        time.sleep(2)
        if opcion2 == 1:
            print("================================================")
            print("Felicidades, Mira si tiene reservacion para 2")
            print("1)Si")
            print("2)No")
            print("================================================")
#Opcion 3
            opcion3 = int(input("Pon tu opcion aqui: "))
            time.sleep(2)
            if opcion3 == 1:
                print("Listo, Has la reservacion")
                break
            elif opcion3 == 2:
                print("No encotraste, vuelve a buscar")
            else:
                print("Opcion no permitida >:c")
        elif opcion2 == 2:
            print("¿No encontraste?, vuelve a buscar")
            print("================================================")
        else:
            print("Opcion no autorizada >:c")    
#Opciones de la primera opcion
    elif opcion == 2:
        print("¿No quieres comer?")
        break
    else:
        print("Opcion no permitida >:c")
        break
    