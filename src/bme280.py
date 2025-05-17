import time
import board
import busio
import adafruit_bme280
import paho.mqtt.client as mqtt

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/bme280'

def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    while True:
        temp = bme280.temperature
        hum = bme280.humidity
        press = bme280.pressure
        payload = f'{{"temperature": {temp:.2f}, "humidity": {hum:.2f}, "pressure": {press:.2f}}}'
        client.publish(MQTT_TOPIC, payload)
        time.sleep(10)

if __name__ == '__main__':
    main()
