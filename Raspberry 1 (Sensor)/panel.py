# Este script debe ser ejecutado como superusuario (sudo su) en Linux
import os, sys, time

while True:
    print ('1. Armar la alarma')
    print ('2. Desarmar la alarma')
    print ('s. Salir')
    choice = raw_input('--> ')
	
    if choice == '1':
        print ('La alarma ha sido activada. 3 minutos para salir de la vivienda')
        time.sleep(180) # 3 minutos
	print ('Camara activada')
        os.system('python camera.py') # Inicia el proceso de la cámara
        sys.exit()
	
    elif choice == '2':
        with open('msgsend.txt','w+') as a:
            a.seek(0)
            a.write('0')
            a.truncate()
	    a.close()
	with open('pidble.txt','w+') as b:
	    b.seek(0)
	    b.write('0')
	    b.truncate()
	    b.close() ## Cambiamos el valor del archivo de alertas y el del PID del proceso Bluetooth a '0', es decir, hacemos un 'reset' al sistema 
	
        print ('La alarma ha sido detenida')
        os.system('pkill python') # Detiene la ejecución de los procesos Python del sistema
        sys.exit()
	
    elif choice == 's':
        sys.exit()

        
