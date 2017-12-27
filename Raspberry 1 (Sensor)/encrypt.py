# Encripta el archivo de vídeo que posteriormente se transmitirá
import os, random, sys
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = "e_video.h264" # Archivo de salida
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ''

	for i in range(16):
		IV += chr(random.randint(0, 0xFF))

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))


def getKey(password):
	hasher = SHA256.new(password)
	return hasher.digest()

def Main():

    while True:
        try:
            filename = 'video.h264' # Archivo de entrada
            password = 'password' # Clave de encriptación
       	    encrypt(getKey(password), filename)
            break
        except:
            print ('Encriptacion fallida')
            break

if __name__ == '__main__':
	Main()


