import machine
import time
from machine import ADC, Pin

light_sensor = ADC(Pin(26))

# Initialize yellow LED
yellow_led = machine.Pin(1, machine.Pin.OUT)

while True:
    light_level = light_sensor.read_u16()  # Reads value from 0 to 65535
    print("Light Level:", light_level)
    time.sleep(0.5)

# TODO: add logic to determine if it's dark or light, maybe add a blue LED to indicate if it's too bright? LED will blink if it's too bright?
# dark_threshold = 1000