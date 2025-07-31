import machine
import time
import dht

class TemperatureSensor:
    def __init__(self):
        # Initialize DHT11 sensor
        self.sensor = dht.DHT11(machine.Pin(27))
        
        # Initialize red LED
        self.red_led = machine.Pin(0, machine.Pin.OUT)
        
        # Intialize green LED
        self.green_led = machine.Pin(2, machine.Pin.OUT)
        
        # Set initial state of the LED
        self.red_led.off()
        self.green_led.off()
    
    def measure_temp(self):
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()

            print("Temperature: {}°C".format(temp))
                
            # Approximate temperature thresholds recommended for best sleep quality (15°C to 20°C)
            if temp < 15:
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
            
    def measure_humidity(self):
        try:
            self.sensor.measure()
            humidity = self.sensor.humidity()
            
            print("Humidity: {}%".format(humidity))
      
            # Approximate humidity thresholds recommended for best sleep quality (30% to 60%)
            if humidity < 30 or humidity > 60:
                print("Current room humidity is outside the recommended range (30% to 60%) for sleep quality")
                self.green_led.on()
                time.sleep(2)
                self.green_led.off()
            else:
                self.green_led.off()
        except OSError as e:
            print("Failed to read from DHT11 sensor:", e)
            time.sleep(2)