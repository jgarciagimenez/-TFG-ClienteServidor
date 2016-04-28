import socket 
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def solicitarNivel():
    #Pendiente de implementar
    return "asdfasdfasdf"

#def solicitarFirewall():
    #Pendiente de implementar

#def solicitarSnort():
    #Pendiente de implementar



    
def defcon(codigo):
    ## Función para cambiar los parámetros del nivel de seguridad.
    
    print ("se ha entradoe en la función defcon para cambiar el nivel de seguridad")
    
def activarDefcon(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   
    print (str(d) +" "+ str(t) + "  Activamos el nivel de seguridad Defcon  " + valor)

    ## Falta por definir los scripts que activen los niveles.

def query(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   

    if(int(valor) == 1):
        respuesta =  solicitarNivel();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 2):
        # solicitarFirewall();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 3):
        # solicitarSnort();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)

    return respuesta

## Creamos las variables con los parámetros para el socket y creamos el socket

udpIP_servidor = '127.0.0.1'
udpPORT_servidor = 4444
udpIP_cliente = '127.0.0.1'
udpPORT_cliente = 4488
sock_escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Iniciamos el socket

sock_escucha.bind ((udpIP_servidor,udpPORT_servidor))

## Cargamos la clave privada para leer los mensajes cifrados.

with open ('clave_privada_servidor.pem','rb') as key_file:
    private_key_server = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
        backend = default_backend()
    )

with open ('clave_publica_cliente.pem','rb') as key_file:
    public_key_client = serialization.load_pem_public_key(
        key_file.read(),
        backend = default_backend()
    )




## Creamos un bucle para que esté escuhando constantenmente

while True :
    

    datos,direccion = sock_escucha.recvfrom(1024)  ## 1024 es el tamaño del buffer           
    cifrado = datos

    descifrado = private_key_server.decrypt(
        cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    
    recibido = descifrado.decode('UTF-8')

    if recibido.startswith("QUERY"):
        recibido = recibido.split(' ', 1)[1]
        respuesta = query(recibido)

        ## Encode the message to send the bytes
            
        mensaje = str.encode(respuesta)

    
    ## Cipher the the encoded message with the server public key 

        cifrado = public_key_client.encrypt(
            mensaje,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        )
            ## Send the encrypted message to the server
        sock_habla.sendto(cifrado,(udpIP_cliente,udpPORT_cliente))



    elif recibido.isdigit():
        activarDefcon(recibido)

    else:
        print("Se ha recibido un mensaje erroneo")

  





  

