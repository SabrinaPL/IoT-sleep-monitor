import machine
import time
import dht

class TemperatureSensor:
    def __init__(self):
        # Initialize DHT11 sensor
        self.sensor = dht.DHT11(machine.Pin(27))
        
        # Initialize red LED
        self.red_led = machine.Pin(0, machine.Pin.OUT)
        
        # Set initial state of the LED
        self.red_led.off()
    
    def run(self):
        while True:
            try:
                self.sensor.measure()
                temp = self.sensor.temperature()
                hum = self.sensor.humidity()
                print("Temperature: {}°C  Humidity: {}%".format(temp, hum))
                
                if temp < 15.6:
                    print("Current room temperature is too low and might negatively affect sleep quality")
                    self.red_led.on()
                    time.sleep(2)
                    self.red_led.off()
                elif temp > 20:
                    print("Current room temperature is too high and might negatively affect sleep quality")
                    self.red_led.on()
                    time.sleep(2)
                    self.red_led.off()
                else:
                    self.red_led.off()
                
            except OSError as e:
                print("Failed to read from DHT11 sensor:", e)
            
            time.sleep(2)