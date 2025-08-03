import machine
import time
from machine import ADC, Pin

class LightSensor:
    def __init__(self):
        # Initialize ADC for light sensor
        self.light_sensor = ADC(Pin(26))
        
        # Initialize yellow LED
        self.yellow_led = machine.Pin(1, machine.Pin.OUT)
        
        self.dark_threshold = 1400  # Threshold for dark environment
        
        # Set initial state of the LED
        self.yellow_led.off()
        
        print("Light sensor initialized on Pin 26")
        
    def measure_light(self):
        try:
            light_level = self.light_sensor.read_u16()  # Reads value from 0 to 65535
            print("Light Level:", light_level)
            time.sleep(0.5)
            
            if light_level > self.dark_threshold:
                print("The room is dark enough for good sleep.")
                self.yellow_led.off()
            else:
                print("It's too bright, you might want to dim the lights for optimal sleep.")
                self.yellow_led.on()
                time.sleep(2)
                self.yellow_led.off()
            
            return light_level 

        except OSError as e:
            print("Failed to read from light sensor:", e)
            return None  # Return None if reading fails