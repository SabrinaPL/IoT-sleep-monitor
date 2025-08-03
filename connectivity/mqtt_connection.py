from connectivity.mqtt import MQTTClient
import keys

def connect_mqtt():
    client = MQTTClient(
        client_id=keys.AIO_CLIENT_ID,
        server=keys.AIO_SERVER,
        port=keys.AIO_PORT,
        user=keys.AIO_USER,
        password=keys.AIO_KEY,
        keepalive=60
    )
    
    try:
        client.connect()
        print("Connected to MQTT broker")
    except Exception as e:
        raise Exception(f"Failed to connect to MQTT broker: {e}")
    
    return client