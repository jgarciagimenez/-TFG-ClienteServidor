import socket 
import time
import os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

#########################################################################
##   Function that return the current alert level of the sensor node   ##
#########################################################################

def solicitarNivel():

    return nivelActual

#########################################################################
##    Function that return the current level of the firewall of the    ##
##          sensor node                                                ##
#########################################################################

def solicitarFirewall():

    if nivelActual[6] == '1' or nivelActual[6] == '2' or nivelActual[6] == '4':
        return "Cortafuegos estricto "
    elif nivelActual[6] == '3':
        return "Cortafuegos medio "
    elif nivelActual[6] == '5' or nivelActual[6] == '6':
        return "Cortafuegos desactivado"


#########################################################################
##    Function that return the current level of snort of the           ##
##              sensor node                                            ##
#########################################################################

def solicitarSnort():

    if nivelActual[6] == '1' or nivelActual[6] == '3' or nivelActual[6] == '5':
        return "Snort estricto "
    elif nivelActual[6] == '2':
        return "Snort medio "
    elif nivelActual[6] == '4' or nivelActual[6] == '6':
        return "Snort desactivado"

#########################################################################
##    Function that activate the security tools acording to the        ##
##     current alert level, in order to activate the different         ##
##     security tools, firt we stop the snort process to start         ##
##     it again with a different rule set. Also, we call a bash        ##
##     script to set the new iptables rule sets                        ##
#########################################################################
    
def activarDefcon(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   
    print (str(d) +" "+ str(t) + "  Activamos el nivel de seguridad Defcon  " + valor)
    respuesta = 'defcon'+valor

   # os.system("pkill snort")  ## Matamos el anterior proceso de snort para iniciar uno nuevo

    if valor == '1':
       print ("sasfasdagsdasg")
       # os.system("./defcon1")        
    if valor == '2':
       print ("sasfasdagsdasg")
       # os.system("./defcon2")
    if valor == '3':
       print ("sasfasdagsdasg")
       # os.system("./defcon3")
    if valor == '4':
       print ("sasfasdagsdasg")
       # os.system("./defcon4")
    if valor == '5':
       print ("sasfasdagsdasg")
       # os.system("./defcon5")
    if valor == '6':
       print ("sasfasdagsdasg")
       # os.system("./defcon6")

    return respuesta



#########################################################################
##    Function that return the answer of the diferent possibles        ##
##    queries the client can send, in order to do that, it calls       ##
##    the 3 functions we have defined above                            ##
#########################################################################

def query(valor):

    t = time.strftime("%H:%M:%S")
    d = time.strftime("%d/%m/%Y")   

    if(int(valor) == 1):
        respuesta =  solicitarNivel();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 2):
        respuesta = solicitarFirewall();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)
    elif(int(valor) == 3):
        respuesta = solicitarSnort();
        print (str(d) +" "+ str(t) + "  Se recibe el mensaje de control  " + valor)

    return respuesta


#########################################################################
##                           MAIN PROGRAM                              ##
#########################################################################



## Definimos lo parámetros para el socket para escuchar y hablar,
## se podrían ingresar por la consola si se desea
## Define the parametres needed to create the listen socket and the talking socket

udpIP_servidor = '127.0.0.1'
udpPORT_servidor = 4444
udpIP_cliente = '127.0.0.1'
udpPORT_cliente = 4488
sock_escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

nivelActual = "6"

## Creamos los  sockets
## Create the sockets

sock_escucha.bind ((udpIP_servidor,udpPORT_servidor))

## Cargamos la clave privada del servidor de un fichero .pem
## Load the private key of the server from a .pem file

with open ('clave_privada_servidor.pem','rb') as key_file:
    private_key_server = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
        backend = default_backend()
    )

## Cargamos la clave pública del cliente de un fichero .pem
## Load the public key of the client from a .pem file

with open ('clave_publica_cliente.pem','rb') as key_file:
    public_key_client = serialization.load_pem_public_key(
        key_file.read(),
        backend = default_backend()
    )



#########################################################################
##                           MAIN LOOP                                 ##
#########################################################################

while True :
    
    ## We wait until we recive a message from the client

    datos,direccion = sock_escucha.recvfrom(1024)  ## 1024 = buffer siza           
    cifrado = datos


    ## We decrypt the message of the client.

    descifrado = private_key_server.decrypt(
        cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    
    recibido = descifrado.decode('UTF-8')

    ## If the message is a query, we enter this if

    if recibido.startswith("QUERY"):
        recibido = recibido.split(' ', 1)[1]
        respuesta = query(recibido)             ## Call the query function to get the answer

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

        ## Now we wait fot the ACK

        try:        

            datos_respuesta,direccion = sock_escucha.recvfrom(1024)
            
            if datos_respuesta.decode('UTF-8') == 'ACK':
                print("Se recibe el ACK")
            else: 
                print ("Se recibe: " + datos_respuesta.decode('UTF-8'))

        except timeout:
            print ("ACK timeout")


    # if the message is an alert level we enter this if

    elif recibido.isdigit():
        
        nivelActual = activarDefcon(recibido)

        ## Send the ACK

        sock_habla.sendto(str.encode("ACK"),(udpIP_cliente,udpPORT_cliente))

    else:
        print("Se ha recibido un mensaje erroneo")

  





  

