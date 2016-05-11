import socket 
import time
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def solicitarNivel():

    return nivelActual


def solicitarFirewall():

    if nivelActual[6] == '1' or nivelActual[6] == '2' or nivelActual[6] == '4':
        return "Cortafuegos estricto "
    elif nivelActual[6] == '3':
        return "Cortafuegos medio "
    elif nivelActual[6] == '5' or nivelActual[6] == '6':
        return "Cortafuegos desactivado"

def solicitarSnort():

    if nivelActual[6] == '1' or nivelActual[6] == '3' or nivelActual[6] == '5':
        return "Snort estricto "
    elif nivelActual[6] == '2':
        return "Snort medio "
    elif nivelActual[6] == '4' or nivelActual[6] == '6':
        return "Snort desactivado"

    
def activarDefcon(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   
    print (str(d) +" "+ str(t) + "  Activamos el nivel de seguridad Defcon  " + valor)
    respuesta = 'defcon'+valor

    os.system("pkill snort")  ## Matamos el anterior proceso de snort para iniciar uno nuevo

    if valor == '1':
        os.system("./defcon1")        
    if valor == '2':
        os.system("./defcon2")
    if valor == '3':
        os.system("./defcon3")
    if valor == '4':
        os.system("./defcon4")
    if valor == '5':
        os.system("./defcon5")
    if valor == '6':
        os.system("./defcon6")

    else : 
        print ("asdfasgdasdfg")
    return respuesta

    ## Falta por definir los scripts que activen los niveles.

def query(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   

    if(int(valor) == 1):
        respuesta =  solicitarNivel();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 2):
        respuesta = solicitarFirewall();
        print ("\n\n\nafañskdjfañsldkjf:" + respuesta + '\n\n\n')
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 3):
        respuesta = solicitarSnort();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)

    return respuesta

## Creamos las variables con los parámetros para el socket y creamos el socket

udpIP_servidor = ''
udpPORT_servidor = 4444
udpIP_cliente = '192.168.1.10'
udpPORT_cliente = 4488
sock_escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

nivelActual = ""

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


        cifrado_respuesta = public_key_client.encrypt(
            mensaje,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None
            )
        )
            ## Send the encrypted message to the server
        sock_habla.sendto(cifrado_respuesta,(udpIP_cliente,udpPORT_cliente))



    elif recibido.isdigit():
        nivelActual = activarDefcon(recibido)

    else:
        print("Se ha recibido un mensaje erroneo")

  





  

