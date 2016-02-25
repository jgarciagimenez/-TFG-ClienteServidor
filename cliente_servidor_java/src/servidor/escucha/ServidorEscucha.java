/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servidor.escucha;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Jose
 */
public class ServidorEscucha {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {       
    
        DatagramSocket socketServidor = null;
        int puerto = 4444;
        
        
        System.out.println("Vamos a lanzar el servidor que esté esuchando en el puerto 4444");
                   
        try {
            socketServidor = new DatagramSocket(puerto);
        } catch (IOException ex) {
            Logger.getLogger(ServidorEscucha.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        byte[] datosRecibidos = new byte[1024];
        
        while (true){
            

            DatagramPacket packetRec = new DatagramPacket(datosRecibidos,datosRecibidos.length);
            
            try {
                socketServidor.receive(packetRec);
            } catch (IOException ex) {
                Logger.getLogger(ServidorEscucha.class.getName()).log(Level.SEVERE, null, ex);
            }
            

           PrintWriter writer = null;
           String fecha = new Date().toString();
           try {
               writer = new PrintWriter("datos sensores.txt", "UTF-8");
           } catch (FileNotFoundException ex) {
               Logger.getLogger(ServidorEscucha.class.getName()).log(Level.SEVERE, null, ex);
           } catch (UnsupportedEncodingException ex) {
               Logger.getLogger(ServidorEscucha.class.getName()).log(Level.SEVERE, null, ex);
           }


            writer.println(fecha +" El sensor mide:" + new String(packetRec.getData()));
            writer.close();
            System.out.println(fecha +" El sensor mide:" + new String( packetRec.getData()));
            
        }       
    }    
}
