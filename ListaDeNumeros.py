#Agregamos librerias
import time
#Aqui iniciamos
#Creamos la variable suma_lista y le definimos las listas
def suma_listas(lista1, lista2):
#Ponemos un valor vacio
    lista_suma = []
#Creamos el bucle
    for i in range(len(lista1)):
#Aqui sumamos las listas 1 y 2
        suma = lista1[i] + lista2[i]
#Esta línea utiliza el método .append() para agregar el valor de la variable suma al final de la lista lista_suma".
        lista_suma.append(suma)
#Este retum nos devuelve la suma que tiene almacenada en la lista 1 y 2
    return lista_suma
#Creamos las listas-
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
#Esta línea llama a la función suma_listas con las listas lista1 y lista2 como argumentos y guarda el resultado en una variable llamada lista_resultado. El resultado es una nueva lista que contiene la suma de los elementos de las listas lista1 y lista2 en la misma posición.
lista_resultado = suma_listas(lista1, lista2)
#Aqui imprimimos
print(lista1)
print(lista2)
print(lista_resultado)