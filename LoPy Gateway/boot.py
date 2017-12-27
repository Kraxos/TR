import os
import machine

uart = machine.UART(0, 115200) # disable these two lines if you don't want serial access
os.dupterm(uart)
