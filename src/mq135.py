# Reads MQ-135 analog value via MCP3008 channel 0, estimates "air quality"
import time
import paho.mqtt.client as mqtt
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/mq135'
MQ135_CHANNEL = 0

SPI_PORT = 0
SPI_DEVICE = 0

def main():
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    while True:
        value = mcp.read_adc(MQ135_CHANNEL)
        payload = f'{{"value": {value}}}'
        client.publish(MQTT_TOPIC, payload)
        time.sleep(10)

if __name__ == '__main__':
    main()
