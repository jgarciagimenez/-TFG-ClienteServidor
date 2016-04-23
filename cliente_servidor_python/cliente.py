import socket
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

## Función para imprimir el menú para que el agente de sguridad eliga el nivel de seguridad

def imprimir_niveles():
	print ("Los niveles a elegir son los siguietes: \n")
	print ("Defcon 1: Cortafuegos estricto y IDS estricto")
	print ("Defcon 2: Cortafuegos estricto y IDS medio")
	print ("Defcon 3: Cortafuegos medio y IDS estricto comment: Adecuado para actualizaciones")
	print ("Defcon 4: Cortafuegos estricto y IDS desactivado")
	print ("Defcon 5: Cortafuegos desactivado y IDS estricto")
	print ("Defcon 6: Cortafuegos desactivado y IDS desactivado \n")


## Definimos lo parámetros para el socket , se podrían ingresar por la consola si se desea

udpIP = "192.168.1.20"
udpPORT = 4444

## Creamos el socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Cargamos la clave pública de un fichero .pem

with open ('clave_publica.pem','rb') as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
	)


while True:

	correcto = False  # Variable para comprobar que el nivel introducido es correcto

	imprimir_niveles()  


## cogemos el valor de la consola hasta que sea uno válido
	while correcto == False:

		defcon = int(input ("Pulsa el número de alerta: "))

		if defcon > 0 and defcon <7:
			correcto = True
		else:
			print (" El nivel introducido es incorrecto. Itroduzca de nuevo el nivel")

## Transmitimos el mensaje de control

			#	mensaje = str.encode('CONTROL sadfasdf')
	mensaje = str.encode(str(defcon))
	print("\n El nivel seleccionado es Defcon " + str(defcon)+ "\n")

				## Ciframos el mensaje con la clave pública

	cifrado = public_key.encrypt(
		mensaje,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA1()),
			algorithm=hashes.SHA1(),
			label=None
		)
	)

	sock.sendto(cifrado,(udpIP,udpPORT))



