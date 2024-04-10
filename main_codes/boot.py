
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import dht
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'isim'
password = 'şifre'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Bağlantı Gerçekleşti')
print(station.ifconfig())


sensor = dht.DHT11(Pin(10)) #örnek olarak pin verildi 



led = Pin(2, Pin.OUT) #örnek olarak pin verildi
