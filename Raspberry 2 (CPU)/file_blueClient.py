# Este programa se encarga de conectar con el servidor que se encuentra en la otra Raspberry, recibir el archivo encriptado e iniciar la desencriptación
import bluetooth, os
import socket
import sys
import time
import shutil

time.sleep(2.5) # Tiempo de espera para que el servidor del otro lado de la transmisión se ejecute
serverMACAddress = 'B8:27:EB:EC:06:47' # Dirección MAC del servidor
port = 3 # Puerto de transmisión
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

while 1:
    filename = 'e_video.h264' # Nombre del archivo que se quiere transmitir
    s.send(filename) # Enviar nombre al servidor
    data = s.recv(1024) # Cantidad de datos recibidos
    if data[:6] == 'EXISTS':
        filesize = long(data[6:]) ## Recibe la confirmación del servidor y el tamaño del archivo
	print (filesize)
        while True:
            try:
                s.send("OK") # Envía confirmación
                f = open(''+filename, 'wb')
                data = s.recv(1024) # Recibe datos
                totalRecv = len(data) 
                f.write(data)
                while totalRecv < filesize: # Si el total de los datos recibidos es menor al del tamaño total del archivo:
                    data = s.recv(1024)
                    totalRecv += len(data) # Recibir datos y sumarlos al total de datos recibidos por parte del cliente
                    f.write(data)
                    print ("{0:.2f}".format((totalRecv/float(filesize))*100)+ "% completado") # Mostrar porcentaje del progreso de la transmisión
                print ("Transmision completada.")
		time.sleep(1.5)
	        pid=os.fork()
	        if pid==0: # Crear un nuevo proceso independiente: desencriptación del archivo
                    os.system('python decrypt.py &')
	            time.sleep(2)
		    exit()
		    sys.exit()
            except socket.error as e:
                if e.errno != errno.ECONNRESET:
                    print ('Error de cliente')
                    break
	        else:
		    pass
    else:
        sys.exit()

