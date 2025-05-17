import time
from w1thermsensor import W1ThermSensor
import paho.mqtt.client as mqtt

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/ds18b20'

def main():
    sensor = W1ThermSensor()
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    while True:
        temp = sensor.get_temperature()
        payload = f'{{"temperature": {temp:.2f}}}'
        client.publish(MQTT_TOPIC, payload)
        time.sleep(10)

if __name__ == '__main__':
    main()
