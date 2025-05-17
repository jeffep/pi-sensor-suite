# Example: Read all 8 channels and publish their values (for debugging)
import time
import paho.mqtt.client as mqtt
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/mcp3008'

SPI_PORT = 0
SPI_DEVICE = 0

def main():
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    while True:
        values = [mcp.read_adc(i) for i in range(8)]
        payload = '{"channels": %s}' % values
        client.publish(MQTT_TOPIC, payload)
        time.sleep(10)

if __name__ == '__main__':
    main()
