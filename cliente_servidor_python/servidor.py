import socket 
import time

    
def defcon(codigo):
    ## Función para cambiar los parámetros del nivel de seguridad.
    
    print ("se ha entradoe en la función defcon para cambiar el nivel de seguridad")
    
   
   
## Creamos las variables con los parámetros para el socket y creamos el socket

udpIP = '127.0.0.1'
udpPORT = 4444
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
estadoEncryp = False

## Iniciamos el socket

sock.bind ((udpIP,udpPORT))

## Creamos un bucle para que esté escuhando constantenmente

while True :
    
    datos,direccion = sock.recvfrom(1024)  ## 1024 es el tamaño del buffer
    recibido = datos.decode("UTF-8")
    outfile = open('sensor_recibido.txt','a')
    
    if recibido.startswith("CONTROL"):
        defcon(recibido)        

    else :
      
        t = time.strftime("%H:%M:%S")
        d = time.strftime("%d/%m/%Y")	
        print (str(d) +" "+ str(t) + "  El sensor recive:  " + recibido)
        outfile.write( "\n" + str(d) +" "+ str(t) + "  El sensor recive: " + recibido)
        outfile.close
    
  

