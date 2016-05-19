import socket
import select

udp_IP = "127.0.0.1"
udp_PORT = 4444


sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	mensaje = input ("introduce: \n")
	ACK = False
	while ACK == False:
		sock_habla.sendto(str.encode(mensaje), (udp_IP, udp_PORT))
		
		sock_habla.setblocking(0)
		ready = select.select([sock_habla], [], [], 2)
		if ready[0]:
			data = sock_habla.recv(4096)
			if data.decode('UTF-8') == "ACK":
				ACK = True
