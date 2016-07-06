from cryptography.fernet import Fernet
import socket
import select

udp_IP = "127.0.0.1"
udp_PORT = 4444

sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


file = open('clave_test', 'r')
keylist  = file.readlines()
key_aux = keylist[0]
key = str.encode(key_aux)
f = Fernet(key)


while True:
	mensaje = input ("introduce: \n")
	mensajeCodificado = str.encode(mensaje)
	mensaje_cifrado = f.encrypt(mensajeCodificado)
	ACK = False
	while ACK == False:
		sock_habla.sendto(mensaje_cifrado, (udp_IP, udp_PORT))
		
		sock_habla.setblocking(0)
		ready = select.select([sock_habla], [], [], 2)
		if ready[0]:
			data = sock_habla.recv(4096)
			if data.decode('UTF-8') == "ACK":
				ACK = True
