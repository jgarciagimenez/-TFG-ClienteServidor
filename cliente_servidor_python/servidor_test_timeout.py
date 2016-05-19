import socket

udp_IP = "127.0.0.1"
udp_PORT = 4444


sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock_habla.bind((udp_IP, udp_PORT))

while True:
	data, addr = sock_habla.recvfrom(1024) # buffer size is 1024 bytes
	print (data.decode("UTF-8"))
	mensaje = input ("introduce: \n")
	sock_habla.sendto(str.encode(mensaje), addr)