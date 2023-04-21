#Aqui se importan las librerias que se necesitan
import time
from tqdm import tqdm
#Aqui inicamos a imprimir lo que necesita comuncar
print("================================================")
print("Bienvenidos a mi Diagrama de como hacer un huevo")
#time.sleep es para darle un delay y adentro de de los parentesis se pone lo segundos
time.sleep(2)

print("¿Quieres aprender a hacer un huevo frito?")
time.sleep(2)

#Imprimimos las opciones
print("1) Si")
print("2) No")
print("================================================")

#Ponemos "I" para saber que es un ingrediente (Aqui la sarten no es un ingrediente pero es necesario para hacer el huevo)
dict = { "i1": "huevos", "i2": "Sarten", "i3": "Sal", "4i": "Aceite", }
#while True es para inicia un bucle 
while True:
#opcion es una variable que tiene un numero entero y donde se puede introoduccir un numero y asi mismo se puede inprimir en pantalla
    opcion = int(input("Pon tu opcion aqui: "))
#Aqui estan las opciones que se pueden seleccionar
    #Aqui esta la primera opcion donde si quiere saber como preparar un huevito
    if opcion == 1:
        print("Entonces si quieres el Huevo frito :D")
#Aqui va una barra de progreso (Añadir en otro momento)
        # pbar = tqdm(total=10)
        # i = 0
        # while i < 10:
        #     time.sleep(1)
        #     pbar.update(1)
        #     i += 1
        #Aqui son sub opciones para el diccionario
        print("================================================")
        print("¿Quieres saber los ingredientes y objetos necesarios?")
        print("1) Si")
        print("2) No")
        subopcion = int(input("Pon tu opcion aqui: "))
        print("================================================")
        if subopcion == 1:
                # for i in dict.items():
                    # print(f"ingredientes: {i}")
                    print(dict)
                    time.sleep(2)
                    print("================================================")
                    print("1)Pon la sarten en la estufa\n 2)Pon un poco de aceite\n 3)Prende la estufa y deja que el aceite se caliente\n 4)Cuando el aceite este caliente rompe el huevo encima de la sarten\n 5)Pon una tapa y espera a que caliente el huevo, toca estar pendiente a que no se queme\n 6)cuando este listo sacarlo en un plato \n 7)ponerle sal(Opcional)\n 8)Disfruta tu huevito frito :D)")
                    break
        #Aqui van las instrucciones para hacer el huevito sin la lista de ingredientes
        elif subopcion == 2:
            print("1)Pon la sarten en la estufa\n 2)Pon un poco de aceite\n 3)Prende la estufa y deja que el aceite se caliente\n 4)Cuando el aceite este caliente rompe el huevo encima de la sarten\n 5)Pon una tapa y espera a que caliente el huevo, toca estar pendiente a que no se queme\n 6)cuando este listo sacarlo en un plato y ponerle sal(Opcional 7)Disfruta tu huevito frito :D)")
            break
        #Accion no permitida
        else:
            print("Esa opcion no esta permitida >:c")
            # pbar.close()
            # break

#Aqui esta la opcion 2 donde no quiere preparar el huevito
    elif opcion == 2:
        print("No te gustan :0")
        break
# Aqui donde pone un valor erroneo 
    else:
        print("Esa opcion no esta permitida >:c")


