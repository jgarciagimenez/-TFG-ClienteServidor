import socket 
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
    
def defcon(codigo):
    ## Función para cambiar los parámetros del nivel de seguridad.
    
    print ("se ha entradoe en la función defcon para cambiar el nivel de seguridad")
    
def activarDefcon(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   
    print (str(d) +" "+ str(t) + "  Activamos el nivel de seguridad Defcon  " + recibido)

    ## Falta por definir los scripts que activen los niveles.




## Creamos las variables con los parámetros para el socket y creamos el socket

udpIP = '127.0.0.1'
udpPORT = 4444
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Iniciamos el socket

sock.bind ((udpIP,udpPORT))

## Cargamos la clave privada para leer los mensajes cifrados.

with open ('clave_privada.pem','rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
        backend = default_backend()
    )


## Creamos un bucle para que esté escuhando constantenmente

while True :
    

    datos,direccion = sock.recvfrom(1024)  ## 1024 es el tamaño del buffer           
    cifrado = datos

    descifrado = private_key.decrypt(
        cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    
    recibido = descifrado.decode('UTF-8')
    activarDefcon(recibido);

   





  

