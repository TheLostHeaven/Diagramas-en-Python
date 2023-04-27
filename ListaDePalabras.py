#Primero que todo ponermos las librerias 
import time
#Ahora que se va a hacer te estaras preguntando, aqui vamos a hacer una lista y en esa lista llevara 50 palabras

palabras = ['Casa', 'Perro', 'Gato', 'Árbol', 'Flor', 'Sol', 'Luna', 'Estrella', 'Cielo', 'Mar', 'Montaña', 'Río', 'Lago', 'Pájaro', 'Pez', 'Libro', 'Lápiz', 'Papel', 'Mesa', 'Silla', 'Puerta', 'Ventana', 'Piso', 'Techo', 'Pared', 'Coche', 'Bicicleta', 'Camión', 'Avión', ',Barco', 'Tren', 'Zapato', 'Calcetín', 'Pantalón', 'Camisa', 'Vestido', 'Sombrero', 'Guante', 'Bufanda', 'Abrigo', 'Cuchara', 'Tenedor', 'Cuchillo', 'Plato', 'Vaso', 'Taza', 'Olla', 'Sartén', 'Cazuela', 'Horno']
#Aqui iniciamos con el programa
print("================================================")
print("Bienvenido a programa que te busca una palabra con solo una letra")
# letra = str(input("Pon una letra para buscar: "))
def palabra_con_letra(letra):
    # palabras = ["manzana", "naranja", "plátano", "fresa"]
    for palabra in palabras:
        if letra in palabra:
            return palabra
    return "No se encontró ninguna palabra con esa letra"

letra_usuario = input("Ingresa una letra: ")
print("================================================")
palabra = palabra_con_letra(letra_usuario)
print(palabra)







