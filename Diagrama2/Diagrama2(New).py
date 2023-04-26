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
checkpoint = 1
checkpoint1 = 1
checkpoint2 = 1
#Aqui iniciamos el bucle con el while true
while True:
#Aqui empezamos a hacer las opciones
    opcion = int(input("Pon aqui tu opcion: "))
    if opcion == 1: 
        print("Preparate y vamos para `alla")
        print("================================================")
        time.sleep(2)
        print("Has lo sigueinten\n 1)entra a tu navegado preferido 'si ya hiciste este paso omitelo'\n 2)Busca 'Restaurante 5 estrellas en bogota'\n 3)Mira las paginas que veas que sean confiables\n 4)Mira la disponibilidad")
        time.sleep(2)
        #Aqui ponemos la variables anidadas
        
        checkpoint += 1
        if checkpoint == 1:() 
        print("================================================")
        print("¿Encotraste algo disponible?")
        print("1) Si")
        print("2) No")
        opcion1 = int(input("Pon aqui tu opcion: "))
        print("================================================")
        if opcion1 == 1: 
            print("Listo sigamos con lo siguiente")
        elif opcion1 == 2:
            print("Listo vuelve a hacer los pasos anteriores")
        else:
            print("Opcion no permitida >:c")
        print("================================================")
        
            opcion2 = int(input ("Pon aqui tu opcion: "))
            if opcion2 == 1: 
                print("")
            elif opcion2 == 2:
                print
            else:
                print("Opcion no permitida >:c")

    elif opcion == 2:
        print("¿No quieres ir a comer?")
        break
    else:
        print("Opcion no permitida")
