/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servidor.escucha;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Jose
 */
public class Cliente {
    
    
    public static void main(String[] args) {       
    
    int puerto = 4444;
    InetAddress direccion = null;
    DatagramPacket datagrama;
    DatagramSocket socketCliente = null;
    byte[] datosEnv = new byte[1024];
    String enviar = null;
    
    try {
        // Inicializamos el socket cliente

        socketCliente = new DatagramSocket();
        
    } catch (SocketException ex) {
        Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
    }
    
    // Lee del teclado la entrada que se quiere enviar.
    
    System.out.println("Hemos lanzado el cliente, a continuación escriba lo que quiere enviar");
    

    // Lee la dirección IP para mandar el datagrama   
    
    try {
        direccion = InetAddress.getByName("127.0.0.1");
    } catch (UnknownHostException ex) {
        Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
    }
    
    while(true){
    
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        try {
             enviar = input.readLine();
        } catch (IOException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }

        // Extraemos los bytes de la frase, preparamos el datagrama y lo enviamos.

        datosEnv = enviar.getBytes();
        datagrama = new DatagramPacket(datosEnv, datosEnv.length,direccion,puerto);

        try {
            socketCliente.send(datagrama);
        } catch (IOException ex) {
            Logger.getLogger(Cliente.class.getName()).log(Level.SEVERE, null, ex);
        }

    }
    }   
}
