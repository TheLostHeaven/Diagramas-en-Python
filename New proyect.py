from progressbar import progressbar
from tqdm import tqdm
import random
import time
from colorama import Fore, Back, Style
#Aqui estaba haciendo algunas pruebas

# print(Fore.RED + 'Este texto es rojo')
# print(Back.GREEN + 'y este tiene fondo verde')
# print(Style.DIM + 'pero este texto es tenue')
# print(Style.RESET_ALL)
# print('de vuelta a la normalidad ahora')

# for i in tqdm(range(100)):
#     time.sleep(0.1)

p = ["python", "Programacion", "Habilidad", "metodo", "lineas de codigo", "java", "html", "Visual", "code", ]

for i in range(1000):
    R = random.choice(p)
    
    print(R)
