import socket
import time

## Definimos lo parámetros para el socket , se podrían ingresar por la consola si se desea

udpIP = "127.0.0.1"
udpPORT = 4444

## Creamos el socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


## Pasamos al bucle donde se transmiten datos periodicamente

while True :

#	mensaje = str.encode('CONTROL sadfasdf')
    mensaje = str.encode("asdfasd")
    sock.sendto(mensaje,(udpIP,udpPORT))
    time.sleep(5)


