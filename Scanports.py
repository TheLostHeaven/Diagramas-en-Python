import sys
import socket


O = socket.gethostbyname(input("Inserte direccion Ip:  "))

print("Escanenando Objetivo..." + O)

try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        R = s.connect_ex((O, port))
        if R == 0:
            print("el puerto {} esta abierto".format(port))
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)