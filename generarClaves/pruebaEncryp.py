from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
## cargamos la clave privada para hacer la prueba

with open ('clave_privada.pem','rb') as key_file:
	private_key = serialization.load_pem_private_key(
		key_file.read(),
		password = None,
		backend = default_backend()
	)

## Cargamos la clave pública para la prueba

with open ('clave_publica.pem','rb') as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()
	)

## Generamos un mensaje de prueba para cifrar

mensaje = "hola, estoy sin encriptar"
print(mensaje+ "\n")

## Ciframos el mensaje con la clave pública.

cifrado = public_key.encrypt(
	mensaje.encode(),
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA1()),
		algorithm=hashes.SHA1(),
		label=None
	)
)
print (str(cifrado) + "\n")

## Desciframos el mensaje con la clave privada

descifrado = private_key.decrypt(
	cifrado,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA1()),
		algorithm=hashes.SHA1(),
		label=None
	)
)

print(descifrado.decode('UTF-8'))


