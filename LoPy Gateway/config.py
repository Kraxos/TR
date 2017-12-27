""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# El Gateway ID serán los 3 primeros bytes de la dirección MAC + 'FFEE' + últimos 3 bytes de la dirección MAC
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'router.eu.thethings.network'
PORT = 1700 

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'WLAN_C670' # Nombre de la red wifi en la que se ha de conectar el gateway
WIFI_PASS = 'BQ18PSIBAMK7MDBO8NDK' # Contraseña de dicha red wifi

# Europa: EU868
LORA_FREQUENCY = 868100000 # Frecuencia = 868.1 MHz
LORA_GW_DR = "SF7BW125" #SF7 => Spreading Factor = 7
LORA_NODE_DR = 5
