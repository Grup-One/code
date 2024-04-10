from machine import Pin
from time import sleep
import dht 

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(16))
ldr = ADC(Pin(0))
role = Pin(14,Pin.OUT)
led = Pin(13,Pin.OUT)




while True:
    try:
        ldr_deger  = ldr.read()
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
    except OSError as e:
        print('Failed to read sensor.')
        








