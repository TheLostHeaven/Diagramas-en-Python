#Primero que todo ponermos las librerias 
import time
#Ahora que se va a hacer te estaras preguntando, aqui vamos a hacer una lista y en esa lista llevara 50 palabras
palabras = ['Casa', 'Perro', 'Gato', 'Árbol', 'Flor', 'Sol', 'Luna', 'Estrella', 'Cielo', 'Mar', 'Montaña', 'Río', 'Lago', 'Pájaro', 'Pez', 'Libro', 'Lápiz', 'Papel', 'Mesa', 'Silla', 'Puerta', 'Ventana', 'Piso', 'Techo', 'Pared', 'Coche', 'Bicicleta', 'Camión', 'Avión', ',Barco', 'Tren', 'Zapato', 'Calcetín', 'Pantalón', 'Camisa', 'Vestido', 'Sombrero', 'Guante', 'Bufanda', 'Abrigo', 'Cuchara', 'Tenedor', 'Cuchillo', 'Plato', 'Vaso', 'Taza', 'Olla', 'Sartén', 'Cazuela', 'Horno']
#Aqui iniciamos con el programa
print("================================================")
print("Bienvenido a programa que te busca una palabra con solo una letra")
#Aqui creamos una funcion que se llame palabra_con_Letra y que toma como argumento una variable "letra"
def palabra_con_letra(letra):
#Aqui hacemos un buble for que se intera en cada elemento de la lista y la variable palabra toma el valor de de uno de los elemento de la lista
    for palabra in palabras:
#Esta línea verifica si la letra ingresada por el usuario está contenida en la palabra actual del bucle for. Si la letra está contenida en la palabra, se ejecutará el código dentro del bloque if.
        if letra in palabra:
#Si la letra está contenida en la palabra, esta línea devuelve la palabra como resultado de la función.
            return palabra
#este return no se va a ver porque todas las letras estan en el diccionario
    return "No se encontró ninguna palabra con esa letra"
#Aqui el usuario puede ingresar la letra quiera 
letra_usuario = input("Ingresa una letra: ")
print("================================================")
#Esta línea llama a la función palabra_con_letra con el argumento letra_usuario, que es la letra ingresada por el usuario. La función devuelve una palabra que contiene la letra ingresada por el usuario o un mensaje indicando que no se encontró ninguna palabra con esa letra. El valor devuelto por la función se guarda en una variable llamada palabra
palabra = palabra_con_letra(letra_usuario)
#Aqui imprime el resultado
print(palabra)







