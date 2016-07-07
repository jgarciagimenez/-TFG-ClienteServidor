#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:

    Builder = None


    def __init__(self):
        
        self.Create = None        
        self.Read = None       
        self.Update = None        
        self.Delete = None

        self.builder = Gtk.Builder()
        self.builder.add_from_file("client_interface.glade")
        self.handlers = {  }


        # Conectamos las señales e iniciamos la aplicación
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("window")


        self.window.show_all()


def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()