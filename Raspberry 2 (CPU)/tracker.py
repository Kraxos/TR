# Detecta la creación de nuevos archivos en el directorio a observar. Si es así, ejecuta el programa de avisos al propietario y a la policía
import time, os, psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "/home/pi/Videos" # Directorio donde se encuentran almacenados los videos

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start() # 
        print ('Deteccion de archivos inciada')
        try:
            while True:
                print ('10 minutos...')
                time.sleep(600) # 10 minutos de espera
                print ('Nada ha sido detectado. Apagando los sistemas...')
                pidobs = str(os.getpid()) # Detecta su PID y el proceso se autodestruye
		print (pidobs)
		p = psutil.Process(int(pidobs))
		p.terminate()

        except:
            self.observer.stop()

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created': # Si se ha creado un archivo: 
            print "Received created event - %s." % event.src_path
            print ('Un archivo nuevo ha sido creado. Ejecutando el sistema de alertas...')
            os.system('python alert.py') # Ejecutar el sistema de alertas
if __name__ == '__main__':
    w = Watcher()
    w.run()



