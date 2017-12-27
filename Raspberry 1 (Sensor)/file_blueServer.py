# Transmite el archivo de vídeo al cliente de la Raspberry 2, que actúa como ordenador central
import bluetooth
import socket
import threading
import os
import sys

hostMACAddress = 'B8:27:EB:EC:06:47' # Dirección MAC del adaptador Bluetooth del servidor (Raspberry 1 - Sensor)
port = 3 # Puerto de transmisión
backlog = 1
size = 1024 # Tamaño de los paquetes a transmitir (1024 bytes)
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

def RetrFile(name, sock):
    filename = sock.recv(1024) # Recibe el nombre del archivo del cliente (Raspberry 2 - Ordenador Central)
    if os.path.isfile(filename): # Si el archivo existe:
        sock.send("EXISTS " + str(os.path.getsize(filename))) # Enviar confirmación al cliente
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f: # Abrir archivo a transmitir
                bytesToSend = f.read(1024) # Leer tamaño total del archivo
                sock.send(bytesToSend) # Enviar archivo
                while bytesToSend != "": # Mientras que el tamaño de los datos enviados no sea igual al de los del archivo total, enviar datos
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
		print ('Transmision completada')
		sys.exit()
    else:
        sock.send("ERR ")

    sock.close()


def Main():

    print ("Esperando al cliente...")
    while True:
        c, addr = s.accept()
        print ("Cliente conectado. MAC:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
	sys.exit()
         
    s.close()
    sys.exit()

if __name__ == '__main__':
    Main()

