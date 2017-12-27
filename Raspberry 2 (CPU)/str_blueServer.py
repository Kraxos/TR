# Este programa recibe el mensaje del cliente (transmisión del mensaje de texto) que se encuentra en el otro lado de la transmisión y ejecuta el cliente (transmisión de vídeo) 
import bluetooth, os, sys, time

hostMACAddress = 'B8:27:EB:68:B0:38' # La dirección MAC del adaptador Bluetooth del servidor (Raspberry 2 - Ordenador Central)
port = 6 # Puerto de transmisión
backlog = 1
size = 1024 # Tamaño de los paquetes a enviar (1024 bytes)

s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

print ('Servidor iniciado. Esperando al cliente...')

try:
    client, clientInfo = s.accept()
    while 1:
	print ('Recibiendo datos')
        data = client.recv(size)
	if data == 'OK': # Intercepta datos del cliente (Raspberry 1 - Sensor)
		print ('Mensaje recibido')
        	print ('Mensaje enviado. Ejecutando cliente... (10s)')
		time.sleep(10)
		os.system('python file_blueClient.py') # Ejecuta el cliente para transmitir el archivo encriptado
	else:
		print ('Error recibiendo el mensaje')

except:
    pass

