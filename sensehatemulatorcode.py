#from sense_emu import SenseHat
import time
from sense_emu import SenseHat

sense=SenseHat()
sense.clear()

while True:
    temp = sense.get_temperature()
    temp= round(temp,2)
    print('temperature =',temp)
    pressure=sense.get_pressure()
    pressure= round(pressure,2)
    print('pressure =',pressure)
    humidity=sense.get_humidity()
    humidity= round(humidity,2)
    print('humdity =',humidity)
    time.sleep(15)
    
    