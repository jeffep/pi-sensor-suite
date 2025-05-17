import time
import paho.mqtt.client as mqtt
import Adafruit_BMP.BMP280 as BMP280

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/bmp280'

def main():
    sensor = BMP280.BMP280()
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    while True:
        temp = sensor.read_temperature()
        pressure = sensor.read_pressure()
        payload = f'{{"temperature": {temp:.2f}, "pressure": {pressure:.2f}}}'
        client.publish(MQTT_TOPIC, payload)
        time.sleep(10)

if __name__ == '__main__':
    main()
