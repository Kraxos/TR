# Este programa sirve para transmitir un mensaje de texto al servidor que se encuentra en el ordenador central, detectar y escribir el PID del proceso en un archivo de texto (pidble.txt), actualizar un archivo de memoria (msgsend.txt) según si el mensaje ya se ha transmitido al otro lado de la conexión y ejecutar el servidor Bluetooth que servirá para realizar la transmisión del archivo de vídeo

import bluetooth, sys, time, os

serverMACAddress = 'B8:27:EB:68:B0:38' # Dirección MAC del adaptador Bluetooth del servidor (Raspberry 2 - Ordenador Central)
port = 6
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

pidstr = str(os.getpid()) # Detectar PID del proceso y escribirlo en el archivo de texto (que es leído por el programa de la cámara)
with open('pidble.txt','w+') as pidfile:
	pidfile.seek(0)
	pidfile.write(pidstr)
	pidfile.truncate()
	pidfile.close()

print ('Cliente iniciado. Enviando mensaje al Servidor')

text = 'OK' # Mensaje de texto a enviar al cliente

while 1:
	with open ('msgsend.txt','r') as alertf: # Detectar nivel de alerta
        	alert = str(alertf.read(1))
        	alertf.close()

	if alert == '0': # Si alerta = 1, transmitir el mensaje de texto y ejecutar el servidor. De lo contrario, detectar cada 5 segundos el nivel de alerta
		print ('No hay intrusiones nuevas')
		time.sleep(5)
	else:	
		with open('msgsend.txt','w+') as afile: # Cambia el nivel de alerta de '1' a '0' para posteriormente dar el aviso al servidor del otro lado de la conexión
                	afile.seek(0)
                        afile.write('0')
                        afile.truncate()
                        nalert = str(afile.read(1))
                        afile.close()
		print ('Enviando mensaje')
		s.send(text)
		print ('Mensaje enviado correctamente. Ejecutando Servidor (3s)')
		time.sleep(3)
		os.system('python file_blueServer.py')

