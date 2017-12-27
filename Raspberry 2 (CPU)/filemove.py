# Este programa tiene la función de renombrar y mover los archivos de vídeo para evitar confusiones entre los diferentes achivos y para tener todos los archivos de vídeo ordenados en una carpeta determinada
import os, shutil, datetime, sys, time

src = '/home/pi/' # Directorio desde el que se copia el archivo	
dst = '/home/pi/Videos/' # Directorio destinatario
filename = 'd_video.h264' # Archivo a renombrar/mover

count = 0 # Contador

create_time = os.path.getctime(filename)
format_time = datetime.datetime.fromtimestamp(create_time)
format_time_string = format_time.strftime("%Y-%m-%d %H.%M.%S")
newfile = format_time_string + '.h264'; ## Detectar fecha de creación y crear el nuevo nombre del archivo

os.rename(filename, newfile); # Renombrar archivo
count = count + 1 # Sumarle un 1 al contador
print(filename.rjust(35) + '    =>    ' + newfile.ljust(35))
print(str(count) + ' archivos han sido renombrados. ') ## Mostrar el nombre y la cantidad de archivos renombrados
time.sleep(1.5)

for basename in os.listdir(src):
        if basename.endswith('.h264'): 
                pathname = os.path.join(src, basename)
                if os.path.isfile(pathname):
                        shutil.move(pathname, dst)
                        time.sleep(2.5) ## Por cada archivo que ermine en '.h264' en el directorio asignado, moverlo en el directorio destinatario
