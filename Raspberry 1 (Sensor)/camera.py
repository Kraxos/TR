# La función de este programa es: 1) detectar movimiento, grabar y crear el archivo de vídeo 2) cambiar un bit de memoria al producirse una detección y 3) detectar si el cliente de texto Bluetooth ya se esta ejecutando en segundo plano y ejecutarlo si dicho proceso no existe

from gpiozero import MotionSensor
from picamera import PiCamera
import os
import time

camera = PiCamera()
pir = MotionSensor(4) #OUT GPIO pin: número 4
while True:
    print ('Sensor de deteccion iniciado') 
    pir.wait_for_motion() # El programa espera hasta que se produzca una detección
    filename = 'video.h264' # El nombre del archivo de video
    print ('Movimiento detectado')

    alertc = str(open('msgsend.txt').read())
    print ('Nivel de alerta: ' + alertc) # Muestra el nivel de alerta actual (0 = no detección // 1 = detección)
    with open('msgsend.txt','w+') as alertf:
        alertf.seek(0)
        alertf.write('1')
        alertf.truncate()
        alertup = str(open('msgsend.txt').read())
        print ('Nuevo nivel de alerta: ' + alertup) # El nivel de alerta cambiará de 0 a 1 y lo escribirá el el archivo de texto
        alertf.close()

    camera.start_recording(filename)
    time.sleep(5) 
    camera.stop_recording() # La grabación dura 5 segundos desde el inicio de la detección
	
    with open ('pidble.txt','r') as pidfile:
        pidproc = str(pidfile.read(1))
        pidfile.close()

    print ('El PID del proceso del cliente Bluetooth es: ' + pidproc) # Lee y muestra el PID del proceso del cliente Bluetooth 

    if pidproc == '0': # Si el proceso del cliente Bluetooth no existe (pidproc = 0) lo ejecutará. De lo contrario solamente ejecutará el programa de encriptación
        
        pid=os.fork()
        if pid==0: 
            os.system("python str_blueClient.py &") # Ejecución del cliente Bluetooth como proceso independiente
            print ('Cliente Bluetooth inicializado')
            os.system('python encrypt.py') # Ejecución del programa de encriptación
            exit()

    elif pidproc != '0':
        print (pidproc)
        print ('El proceso ya se esta ejecutando')
	os.system('python encrypt.py')

    else:
        print ('Error')
