#Como siempre importamos librerias :D
import time

print("================================================")
#Aqui hacemos nuestra lista de frutas
Lista = ['Manzana', 'Pera', 'Mandarinas', 'Uvas', 'Melones']
#En este for hacemos que la lista salga interaro la lista
for Frutas in Lista:
#En este for hacemos que de que en la lista de frutas se imprima con cada letra que se confoma las frutas
    for letra in Frutas:
        print(Frutas)
        print(letra)
#Aqui le damos un pequeño delay al imprimir
        time.sleep(0.1)
        print("================================================")