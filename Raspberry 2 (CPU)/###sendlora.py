# Este programa permite establecer una conexión con LoPy mediante serial access (UART) y enviar datos
import serial, sys, os, datetime, shutil, time

with serial.Serial('/dev/serial0', 115200, timeout=10) as ser: # Detecta la conexión del puerto serial UART (conexión cableada Raspberry - LoPy)
    ser.write(b'send') # Envía datos

print("Datos enviados")



