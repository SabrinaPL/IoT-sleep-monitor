from sensor_modules.temp_sensor import *
from sensor_modules.light_sensor import *

light_sensor = LightSensor()
temp_sensor = TemperatureSensor()

print("Starting sensor measurements...")

while True:
    light_sensor.measure_light()
    temp_sensor.measure_temp()
    temp_sensor.measure_humidity()
    time.sleep(5)




