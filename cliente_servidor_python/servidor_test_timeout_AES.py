import socket
import select
from cryptography.fernet import Fernet


file = open('clave_test', 'r')
keylist  = file.readlines()
key_aux = keylist[0]
key = str.encode(key_aux)

f = Fernet(key)

udp_IP = "127.0.0.1"
udp_PORT = 4444


sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock_habla.bind((udp_IP, udp_PORT))

while True:
	data, addr = sock_habla.recvfrom(1024) # buffer size is 1024 bytes
	decodificado = f.decrypt(data)
	print (decodificado.decode("UTF-8"))
	mensaje = "ACK"
	sock_habla.sendto(str.encode(mensaje), addr)