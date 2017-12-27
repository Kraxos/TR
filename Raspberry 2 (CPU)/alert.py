# Este programa tiene la función de alertar al propietario y enviar datos a LoPy para su transmisión
import urllib, os
import serial, sys, datetime, shutil, time
from twilio.rest import Client

try :
    stri = "https://www.google.com" # Detecta si existe una conexión a Internet
    data = urllib.urlopen(stri)
    print ("Conexion a Internet detectada")

    account_sid = "ACb64cbc3407b6970f1d5ea5a1211bfc95" # Parámetros específicos generados al crear una cuenta en Twilio
    auth_token = "c85b3e89ccc4e07e9089d6731c42ece5"
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
    to="+34620710697", # El destinatario del mensaje SMS, puede ser cualquier número de teléfono real como, por ejemplo, el del propietario
    from_="+34960160696", # Número de la cuenta de Twilio desde el que se ha generado el mensaje. 
    body="Intrusion detectada. Avisando a policia")
    time.sleep(2)

    print ('SMS transmitido. Enviando datos a LoPy')
    with serial.Serial('/dev/serial0', 115200, timeout=10) as ser: # Detecta la conexión del puerto serial UART (conexión cableada Raspberry - LoPy)
    ser.write(b'send') # Envía datos

    print("Datos enviados")

except:
    print ('No se puede conectar a Internet. Enviando datos a LoPy...')
    time.sleep(2)
    with serial.Serial('/dev/serial0', 115200, timeout=10) as ser: 
    ser.write(b'send')

    print("Datos enviados")



