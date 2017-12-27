# Este programa se encarga de desencriptar el archivo ya transmitido y eliminar el archivo encriptado
import os, random, sys, time, shutil
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def decrypt(key, filename):
	chunksize = 64*1024
	outputFile = 'd_video.h264' # Archivo de salida
	
	with open(filename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)


def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()

def Main():
	
    while True:
        try:
            filename = 'e_video.h264' # Archivo de entrada
            password = 'password' # Clave de encriptación
            decrypt(getKey(password), filename)
	    time.sleep(3)
            print "Video desencriptado correctamente"
            os.system('rm e_video.h264') # Eliminar archivo encriptado
	    time.sleep(3)
            os.system('python filemove.py') # Abrir programa para renombrar y mover el archivo a la carpeta correspondiente
        except:
            pass
	    print "Desencriptacion fallida"
            break

if __name__ == '__main__':
	Main()


