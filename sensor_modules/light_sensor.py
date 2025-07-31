import machine
import time
from machine import ADC, Pin

class LightSensor:
    def __init__(self):
        # Initialize ADC for light sensor
        self.light_sensor = ADC(Pin(26))
        
        # Initialize yellow LED
        self.yellow_led = machine.Pin(1, machine.Pin.OUT)
        
        self.dark_threshold = 1000  # Threshold for dark environment
        
        # Set initial state of the LED
        self.yellow_led.off()
        
    def measure_light(self):
        try:
            light_level = self.light_sensor.read_u16()  # Reads value from 0 to 65535
            print("Light Level:", light_level)
            time.sleep(0.5)
            
            if light_level < self.dark_threshold:
                print("It's dark, you can sleep well.")
                self.yellow_led.off()
            else:
                print("It's bright, you might want to dim the lights for optimal sleep.")
                self.yellow_led.on()
                time.sleep(2)
                self.yellow_led.off()

        except OSError as e:
            print("Failed to read from light sensor:", e)