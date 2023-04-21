#Librerias 
import time
#Inicio del diagrama
print("================================================")
print("Bienvenidos a mi Diagrama de como hacer una reservacion de un restaurante en linea")
print("================================================")
print("¿Quieres ir a comer en un restaurante?")
print("1)Si")
print("2)No")
print("================================================")
#Aqui podemos porner como un tipo de checkpoins para no hacer muchas SubOpciones
checkpoint = False
checkpoint1 = False
#Iniciio el "while True" se puede tratar como una cajita los "if" "elif", "else" se pueden tratar como funciones
while True:
    #Opcion principa
    opcion = int(input("Pon tu opcion aqui: "))
    if opcion == 1:
        print("Ufff, vamos para àlla")
        print("================================================")
        time.sleep(2)
        print("Listo, has lo siguiente")
        print("Prende tu computador\n Entra al navegador de tu preferencia\n Busca'Restaurante 5 estrellas en bogotà'\n entre a la pagina que veas que tiene buena reseñas y que sea confiable\n Mira la disponibilidad")
        time.sleep(2)
        checkpoint = True
        break

            print("================================================")
            print("¿Encotraste algun buen restaurante?")
            print("1)Si")
            print("2)No")

        #Inicio de la SubOpcion
        subopcion = int(input("Pon aqui tu opcion: "))
        #opcion 1 cuando si se encuetra
                if subopcion == 1:
                    print("================================================")
                    print("¿Esta disponible para las 8?")
                    print("1)Si")
                    print("2)No")
        #opcion 2 Cuando no se encuentra
                elif subopcion == 2:
                    print("Listo, vuelve a buscar en el navegador\n Busca'Restaurante 5 estrellas en bogotà'\n entre a la pagina que veas que tiene buena reseñas y que sea confiable\n Mira la disponibilidad")
        #Opcion no permitida
                else:
                    print("Opcion no permitida")
        #Final de la SupOpcion
                #Se vuelve a preguntar
            #Inicio de la SubOpcion1
        subopcion1 = int(input("Pon tu opcion aqui: "))
                if subopcion1 == 1:
                    print("Listo podemos seguir con lo demas")
                    print("================================================")
                elif subopcion1 == 2:
                    print("Listo, vuelve a buscar en el navegador\n Busca'Restaurante 5 estrellas en bogotà'\n entre a la pagina que veas que tiene buena reseñas y que sea confiable\n Mira la disponibilidad")
                else:
                    print("Opcion no permitida")
            #Fin de la SubOpcion1
                print("================================================")
                print("Listo, Sigamos ¿tiene mesas para 2?")
                print("1)Si")
                print("2)No")
                #inicio de la SubOpcion2
                subopcion2 = int(input("Pon tu opcion aqui: "))
        #opcion 2 cuando no se encuetra puede ser una alternativa
                if subopcion2 == 1:
                    print("Listo has tu reserva :D")
                    break
                elif subopcion2 == 2:
                    print("Busca'Restaurante 5 estrellas en bogotà'\n entre a la pagina que veas que tiene buena reseñas y que sea confiable\n Mira la disponibilidad")
        #Accion no permitida
                else:
                    print("Opcion no permitida >:c")
                
#Opciones 2(No), introduccion de una opcion incorrecta
    elif opcion == 2:
        print("¿No quieres ir a comer? :c")
        break
    else:
        print("Opcion no permitida >:c")
    #Final del la Opcion principal