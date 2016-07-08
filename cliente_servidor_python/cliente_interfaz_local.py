#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import socket
import time
import select

# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet


#########################################################################
##                           MAIN PROGRAM                              ##
#########################################################################


## Definimos lo parámetros para el socket para escuchar y hablar , se podrían ingresar por la consola si se desea
## Define the parametres needed to create the listen socket and the talking socket

udpIP_servidor = "127.0.0.1"
udpPORT_servidor = 4444
query = False 
udpIP_cliente = "127.0.0.1"
udpPORT_cliente = 4488

## Creamos los  sockets
## Create the sockets

sock_habla = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_escucha = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

## Iniciamos el socket para escuchar
sock_escucha.bind ((udpIP_cliente,udpPORT_cliente))



## Cargamos la clave pública del servidor de un fichero .pem
## Load the public key of the server from a .pem file


file = open('clave_test', 'r')
keylist  = file.readlines()
key_aux = keylist[0]
key = str.encode(key_aux)
f = Fernet(key)


class Handler:

	Builder = None
	


	def __init__(self):
		

		self.builder = Gtk.Builder()
		self.builder.add_from_file("client_interface.glade")
		self.handlers = {"on_window_destroy": self.on_window_destroy,
						 "on_btn_nivel6_clicked": self.on_btn_nivel6_clicked,
						 "on_btn_nivel5_clicked": self.on_btn_nivel5_clicked,
						 "on_btn_nivel4_clicked": self.on_btn_nivel4_clicked,
						 "on_btn_nivel3_clicked": self.on_btn_nivel3_clicked,
						 "on_btn_nivel2_clicked": self.on_btn_nivel2_clicked,
						 "on_btn_nivel1_clicked": self.on_btn_nivel1_clicked,
						 "on_btn_nivelAct_clicked": self.on_btn_nivelAct_clicked,
						 "on_btn_nivelFW_clicked": self.on_btn_nivelFW_clicked,
						 "on_btn_nivelIDS_clicked": self.on_btn_nivelIDS_clicked } 															


		# Conectamos las señales e iniciamos la aplicación
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("window")
		self.servidor_text = self.builder.get_object("servidor_text")
		self.barra_nivel = self.builder.get_object("barra_nivel")
		self.cliente_text = self.builder.get_object("cliente_text")
		self.window.show_all()
		self.text_cliente = "\n.\n.\n.\n.\n.\n.\n.\n"
		self.text_server = "\n.\n.\n.\n.\n.\n.\n.\n"


	def esperar_respuesta_query(self,codigo,*args):


		mensaje = str.encode(codigo)
		cifrado = f.encrypt(mensaje)

		Contestacion = False

		while not Contestacion:

			sock_habla.sendto(cifrado,(udpIP_servidor,udpPORT_servidor))
			sock_escucha.setblocking(0)
			ready = select.select([sock_escucha], [], [], 2)

			if ready[0]:
				datos_respuesta,direccion = sock_escucha.recvfrom(4096)
				query_cifrado = datos_respuesta
				descifrado = f.decrypt(query_cifrado)

				line_add = "\n El servidor recibe --> " + codigo
				lines = self.text_server.split('\n')
				text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
				self.text_server = text
				self.servidor_text.get_buffer().set_text(text)


				self.add_text_server(descifrado.decode('UTF-8'))
				line_add = "\n El cliente recibe --> " + descifrado.decode('UTF-8') 
				lines = self.text_cliente.split('\n')
				text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
				self.text_cliente = text
				self.cliente_text.get_buffer().set_text(text)


				## When we receive the query and send the ACK
				sock_habla.sendto(str.encode("ACK"),(udpIP_servidor,udpPORT_servidor))
				self.add_text_cliente("ACK \n")

				line_add = "\n El servidor recibe --> " + "ACK \n"
				lines = self.text_server.split('\n')
				text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
				self.text_server = text
				self.servidor_text.get_buffer().set_text(text)

				Contestacion = True
				
				# if defcon[6] == "1":
				# 	imprimir_escala(int(descifrado))

				# else:

				# 	print (" La contestación del servidor es : " + descifrado.decode('UTF-8'))
				


	def esperar_ack_nivel(self,codigo,*args):

		mensaje = str.encode(codigo)
		cifrado = f.encrypt(mensaje)

		ACK_NIVEL = False

		while not ACK_NIVEL:

		
			sock_habla.sendto(cifrado,(udpIP_servidor,udpPORT_servidor))
			sock_escucha.setblocking(0)
			ready = select.select([sock_escucha], [], [], 2)

			if ready[0]:
				
				datos_respuesta,direccion = sock_escucha.recvfrom(4096)

				line_add = "\n El servidor recibe --> " + codigo
				lines = self.text_server.split('\n')
				text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
				self.text_server = text
				self.servidor_text.get_buffer().set_text(text)


				self.add_text_server(datos_respuesta.decode('UTF-8') + "\n")

				line_add = "\n El cliente recibe --> " + datos_respuesta.decode('UTF-8') + "\n"
				lines = self.text_cliente.split('\n')
				text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
				self.text_cliente = text
				self.cliente_text.get_buffer().set_text(text)

				if datos_respuesta.decode('UTF-8') == "ACK":
					print("Se recibe el ACK")
					ACK_NIVEL = True

				else: 
					print ("Se recibe: " + datos_respuesta.decode('UTF-8'))

	def add_text_cliente(self,mensaje,*args):

		line_add = "\n El cliente envia -->  " + mensaje
		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
		self.text_cliente = text
		self.cliente_text.get_buffer().set_text(text)

	def add_text_server(self,mensaje,*args):

		line_add = "\n El servidor envia -->  " + mensaje
		lines = self.text_server.split('\n')
		text = "\n"+lines[-8] +"\n"+lines[-7] +"\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
		self.text_server = text
		self.servidor_text.get_buffer().set_text(text)


	def on_window_destroy(self, *args):
		print ('Se ha cerrado la ventana')
		Gtk.main_quit(*args)

	def on_btn_nivel6_clicked(self,*args):

		mensaje = "1"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(1)

	def on_btn_nivel5_clicked(self,*args):

		mensaje = "2"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(0.75)


	def on_btn_nivel4_clicked(self,*args):

		mensaje = "3"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(0.57)

	def on_btn_nivel3_clicked(self,*args):

		mensaje = "4"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(0.42)

	def on_btn_nivel2_clicked(self,*args):

		mensaje = "5"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(0.27)

	def on_btn_nivel1_clicked(self,*args):

		mensaje = "6"

		self.add_text_cliente(mensaje)
		self.esperar_ack_nivel(mensaje)
		self.barra_nivel.set_fraction(0.11)

	def on_btn_nivelAct_clicked(self,*args):
		
		mensaje = "QUERY 1"
		self.add_text_cliente(mensaje)
		self.esperar_respuesta_query(mensaje)


	def on_btn_nivelFW_clicked(self,*args):

		mensaje = "QUERY 2"
		self.add_text_cliente(mensaje)
		self.esperar_respuesta_query(mensaje)


	def on_btn_nivelIDS_clicked(self,*args):


		mensaje = "QUERY 3"
		self.add_text_cliente(mensaje)
		self.esperar_respuesta_query(mensaje)




def main():

	window = Handler()
	Gtk.main()
	return 0

if __name__ == '__main__':
	main()