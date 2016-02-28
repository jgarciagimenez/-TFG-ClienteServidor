import socket
import time

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

## Definimos lo parámetros para el socket , se podrían ingresar por la consola si se desea

udpIP = "127.0.0.1"
udpPORT = 4444

## Creamos el socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Cargamos la clave pública de un fichero .pem

with open ('clave_publica.pem','rb') as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
	)


## Pasamos al bucle donde se transmiten datos periodicamente

while True :

			#	mensaje = str.encode('CONTROL sadfasdf')
	mensaje = str.encode("asdfasd")

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
	time.sleep(5)


