import os, time, sys, shutil, datetime 
import psutil

dstdr = '/home/pi/Videos'
srcdr = '/home/pi'
extensions = (['.h264']);
filelist = os.listdir( dstdr )
# Move file from source directory to working diretory and rename it accordingly to the creation date (fileRename.py)
# shutil.move (srcdr, wrkdr)

newfilesDictionary = {}

count = 0

#time.sleep(75)
os.system('rm e_video.h264')
	
for basename in os.listdir(srcdr):
        if basename.endswith('.h264'):
                pathname = os.path.join(srcdr, basename)
                if os.path.isfile(pathname):
                        shutil.copy2(pathname, dstdr)
                        time.sleep(2.5)
			print ('Los archivos han sido movidos')

for file in filelist:
        filename, extension = os.path.splitext(file)
        if ( extension in extensions ):
                create_time = os.path.getctime( file )
                format_time = datetime.datetime.fromtimestamp( create_time )
                format_time_string = format_time.strftime("%Y-%m-%d %H.%M.%S")
                newfile = format_time_string + extension;

                if ( newfile in newfilesDictionary.keys() ):
                        index = newfilesDictionary[newfile] + 1;
                        newfilesDictionary[newfile] = index;
                        newfile = format_time_string + '-' + str(index) + extension;
                else:
                        newfilesDictionary[newfile] = 0;

                os.rename( file, newfile );
                count = count + 1
                print( file.rjust(35) + '    =>    ' + newfile.ljust(35) )


print(str(count) + ' archivos han sido renombrados. ')
time.sleep(1.5)


filepid = open('pidble.txt','r')
pidsrv = filepid.read()
print (pidsrv)

p = psutil.Process(int(pidsrv))
p.terminate()
os.system('rm pidble.txt')

print ('Proceso eliminado')
time.sleep(0.5)
#print ('Esperando 10 minutos...')
#time.sleep(600)
#print ('10 minutos transcurridos')
