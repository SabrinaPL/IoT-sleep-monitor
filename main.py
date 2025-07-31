from sensor_modules.temp_sensor import *
from sensor_modules.light_sensor import *

temp_sensor = TemperatureSensor()
light_sensor = LightSensor()

# Add button to start the sensors, then a while loop to keep them running as long as the button is toggled on


temp_sensor.measure_temp()
light_sensor.measure_light()


