from sensor_modules.temp_sensor import TemperatureSensor
from sensor_modules.light_sensor import LightSensor
from connectivity import wifi_connection as wifi, mqtt_connection as mqtt
import keys
import time

print("Starting IoT Sleep Environment Monitor...")

# Initialize sensors
print("Initializing sensors...")
light_sensor = LightSensor()
temp_sensor = TemperatureSensor()

# Connect to WiFi
try:
    print("Connecting to WiFi...")
    ip = wifi.connect()
except Exception as e:
    print("Failed to connect to WiFi:", e)
    
# Connect to MQTT broker
try:
    print("Connecting to MQTT broker...")
    mqtt_client = mqtt.connect_mqtt()
except Exception as e:
    print("Failed to connect to MQTT broker:", e)

# Add function to send data to Adafruit IO

print("Starting sensor measurements...")

while True:
    light = light_sensor.measure_light()
    temperature = temp_sensor.measure_temp()
    humidity = temp_sensor.measure_humidity()

    # Send data to Adafruit IO only if all readings are successful
    if light is not None and temperature is not None and humidity is not None:
        try:
            mqtt_client.publish(keys.AIO_LIGHTS_FEED, str(light))
            mqtt_client.publish(keys.AIO_TEMPERATURE_FEED, str(temperature))
            mqtt_client.publish(keys.AIO_HUMIDITY_FEED, str(humidity))
            print("Data sent to Adafruit IO successfully!")
        except Exception as e:
            print("Failed to send data to Adafruit IO:", e)
    else:
        print("Skipping MQTT publish due to sensor reading failure")
        
    time.sleep(5)  # Delay between measurements
