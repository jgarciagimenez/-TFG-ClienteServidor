import socket
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

## Función para imprimir el menú para que el agente de sguridad eliga el nivel de seguridad
## Function to print the menu to select the differents levles of security and queries to the server 

def imprimir_niveles():
	print ("Los niveles a elegir son los siguietes: \n")
	print ("Defcon 1: Cortafuegos estricto y IDS estricto")
	print ("Defcon 2: Cortafuegos estricto y IDS medio")
	print ("Defcon 3: Cortafuegos medio y IDS estricto comment: Adecuado para actualizaciones")
	print ("Defcon 4: Cortafuegos estricto y IDS desactivado")
	print ("Defcon 5: Cortafuegos desactivado y IDS estricto")
	print ("Defcon 6: Cortafuegos desactivado y IDS desactivado \n")
	print (" Para hacer una peticion insertar: QUERY + codigo peticion \n Las diferentes peticiones son:\n  ")
	print (" -- 1: Solicitar nivel activado actualmente")
	print (" -- 2: Solicitar configuración firewall actual")
	print (" -- 3: Solicitar configuración snort actual")


## Definimos lo parámetros para el socket para escuchar y hablar , se podrían ingresar por la consola si se desea
## Define the parametres needed to create the listen socket and the talking socket

udpIP_servidor = "192.168.1.20"
udpPORT_servidor = 4444
query = False 
udpIP_cliente = ""
udpPORT_cliente = 4488

## Creamos los  sockets
## Create the sockets

sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Iniciamos el socket para escuchar
sock_escucha.bind ((udpIP_cliente,udpPORT_cliente))


## Cargamos la clave pública del servidor de un fichero .pem
## Load the public key of the server from a .pem file

with open ('clave_publica_servidor.pem','rb') as key_file:
	public_key_server = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
	)

## Cargamos nuestra clave privada de un fichero.pem
## Load our private key from a .pem file

with open ('clave_privada_cliente.pem','rb') as key_file:
    private_key_client = serialization.load_pem_private_key(
        key_file.read(),
        password = None,
        backend = default_backend()
    )



while True:

	correcto = False  # var to check if the user input is correct
	query = False   # var to check if the message is a query
	input ("\n Pulsa enter para desplegar el menu ")

	imprimir_niveles()  


## take the input from console until there is a valid input
	while correcto == False:

		defcon = input ("\n Pulsa el número de alerta o intrudce QUERY + orden ")

		if defcon.startswith("QUERY") and defcon.split(' ', 1)[1].isdigit() and int(defcon.split(' ', 1)[1]) > 0 and int(defcon.split(' ', 1)[1]) <4 :
			query = True
			correcto = True

		elif defcon.isdigit() and int(defcon) > 0 and int(defcon) <7:
			correcto = True
		else:
			print ("El comando introducido es incorrecto. Itroduzca de nuevo el comando\n")


## Encode the message to send the bytes
			
	mensaje = str.encode(str(defcon))

	
	## Cipher the the encoded message with the server public key 

	cifrado = public_key_server.encrypt(
		mensaje,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA1()),
			algorithm=hashes.SHA1(),
			label=None
		)
	)

	## Send the encrypted message to the server
	sock_habla.sendto(cifrado,(udpIP_servidor,udpPORT_servidor))



	if query :
		print("\n Se manda el mensaje de query " + defcon+ "\n")

		## Receive the answer for the Query

		datos_respuesta,direccion = sock_escucha.recvfrom(1024)  ## 1024 es el tamaño del buffer           
		query_cifrado = datos_respuesta

		## Decrypt the answer

		descifrado = private_key_client.decrypt(
			query_cifrado,
			padding.OAEP(
				mgf=padding.MGF1(algorithm=hashes.SHA1()),
				algorithm=hashes.SHA1(),
				label=None
			)
		)

		print (" La contestación del servidor es : " + descifrado.decode('UTF-8'))
    
	else : 
		print("\n Se manda el nivel " + defcon)








