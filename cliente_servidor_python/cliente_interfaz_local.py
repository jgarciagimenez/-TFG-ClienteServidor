#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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
		self.cliente_text = self.builder.get_object("cliente_text")
		self.window.show_all()
		self.text_cliente = "\n.\n.\n.\n.\n.\n"

	def on_window_destroy(self, *args):
		print ('Se ha cerrado la ventana')
		Gtk.main_quit(*args)

	def on_btn_nivel6_clicked(self,*args):

		line_add = "\n Se ha activado el nivel6"
		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + line_add
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivel5_clicked(self,*args):

		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + "\n Se ha activado el nivel5"
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivel4_clicked(self,*args):

		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + "\n Se ha activado el nivel4"
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivel3_clicked(self,*args):

		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + "\n Se ha activado el nivel3"
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivel2_clicked(self,*args):

		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + "\n Se ha activado el nivel2"
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivel1_clicked(self,*args):

		lines = self.text_cliente.split('\n')
		text = "\n"+lines[-6] + "\n"+lines[-5] + "\n"+lines[-4] + "\n"+lines[-3] + "\n"+ lines[-2] +"\n"+lines [-1] + "\n Se ha activado el nivel1"
		self.text_cliente = text
		self.servidor_text.get_buffer().set_text(text)

	def on_btn_nivelAct_clicked(self,*args):
		self.cliente_text.get_buffer().insert(self.cliente_text.get_buffer().get_end_iter(), "\n" + "Se ha activado la peticion del nivel")
		print ("Se ha activado la peticion del nivel")

	def on_btn_nivelFW_clicked(self,*args):
		self.cliente_text.get_buffer().insert(self.cliente_text.get_buffer().get_end_iter(), "\n" + "Se ha activado la peticion del Firewall")
		print ("Se ha activado la peticion del Firewall")

	def on_btn_nivelIDS_clicked(self,*args):
		self.cliente_text.get_buffer().insert(self.cliente_text.get_buffer().get_end_iter(), "\n" + "Se ha activado la peticion del IDS")
		print ("Se ha activado la peticion del IDS")




def main():
	window = Handler()
	Gtk.main()
	return 0

if __name__ == '__main__':
	main()