#Iniciamos poniendo librerias
import time

#Programa donde recibe una cadena de caracteres y que me muestre cada letra en una linea distinta utilizando for
list = ["Arroz", "Llanta", "Metodos", "Listas", "Manzanas"]
print("================================================")
print("Bienvenido al programa para separar letra por letra las palabras que pongas")
print("1) Aqui puedes ver un ejemplo")
print("2) Aqui puedes escribir")
print("================================================")
opcion = int(input("Pon aqui tu opcion: "))
if opcion == 1:
    for item in list:
        for letras in item:
            print(letras)
            print("================================================")
elif opcion == 2:
    palabra = str(input("Pon aqui tu palabra: "))
    for item2 in palabra:
        for letras2 in item2:
            print(letras2)
            print("================================================")
else:
    print("opcion no permitida >:c")

