import socket 
import datetime

## Creamos las variables con los parámetros para el socket y creamos el socket

udpIP = '127.0.0.1'
udpPORT = 4444
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Iniciamos el socket

sock.bind ((udpIP,udpPORT))

## Creamos un bucle para que esté escuhando constantenmente

while True :

	t = datetime.time(1,2,3)
	datos,direccion = sock.recvfrom(1024)  ## 1024 es el tamaño del buffer
	print (str(t)+"  El sensor recive:  " + str(datos))