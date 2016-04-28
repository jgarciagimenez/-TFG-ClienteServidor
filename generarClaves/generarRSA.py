from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 1024,
    backend = default_backend()
)
public_key = private_key.public_key()

## Serialización de la clave privada

private_key_ser = private_key.private_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm = serialization.NoEncryption()
)

## Serialización de la clave pública

public_key_ser = public_key.public_bytes(
	encoding = serialization.Encoding.PEM,
	format = serialization.PublicFormat.SubjectPublicKeyInfo
)


outfile = open('clave_privada_servidor.pem','wb')
outfile.write(private_key_ser)
outfile.close

outfile = open('clave_publica_servidor.pem','wb')
outfile.write(public_key_ser)
outfile.close

