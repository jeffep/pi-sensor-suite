````markdown name=README.md
# pi-sensor-suite

A Raspberry Pi 5 project for environmental monitoring and automation using multiple sensors and MQTT.  
This suite supports BMP280, BME280, MQ-135 (via MCP3008 ADC), DS18B20, MCP3008, and HC-SR501 (motion sensor, triggers Pi Camera).  
Sensor data is published to an MQTT broker for integration with home automation, dashboards, or data logging.

---

## Features

- **BMP280 / BME280:** Atmospheric pressure, temperature (and humidity for BME280)
- **MQ-135:** Air quality/gas sensor (analog, via MCP3008 ADC)
- **DS18B20:** Digital temperature sensor (1-Wire)
- **MCP3008:** 8-channel ADC for analog sensors
- **HC-SR501:** PIR motion detector (triggers camera and MQTT event)
- **Camera:** Captures photos when motion is detected
- **MQTT:** All sensors publish data to a broker (defaults to `jarvis` @ 192.168.87.99)

---

## Hardware Wiring / GPIO Pinout

| Sensor/Module      | GPIO Pin(s) Used     | Notes                                       |
|--------------------|----------------------|---------------------------------------------|
| BMP280 / BME280    | I2C: SCL (GPIO 3), SDA (GPIO 2), 3.3V (Pin 1), GND (Pin 6) | Both can share I2C bus                      |
| MCP3008 (ADC)      | SPI: MOSI (GPIO 10, Pin 19), MISO (GPIO 9, Pin 21), SCLK (GPIO 11, Pin 23), CE0 (GPIO 8, Pin 24), 3.3V (Pin 1), GND (Pin 20) | For analog sensors like MQ-135 |
| MQ-135             | MCP3008 CH0          | Connect analog output to MCP3008 channel 0  |
| DS18B20            | GPIO 4 (Pin 7), 3.3V (Pin 1), GND (Pin 9) | 1-Wire, add 4.7kΩ pull-up resistor          |
| HC-SR501 PIR       | GPIO 17 (Pin 11), 3.3V (Pin 1), GND (Pin 6) | OUT → GPIO 17; VCC must be 3.3V             |
| Pi Camera          | Camera Port (CSI)    | Dedicated connector, not GPIO               |

### ASCII Pinout Reference

```
      +------------------------+
 3.3V | [ 1] [ 2] | 5V         |
 SDA  | [ 3] [ 4] | 5V         |
 SCL  | [ 5] [ 6] | GND        |
GPIO 4| [ 7] [ 8] | GPIO 14    |
 GND  | [ 9] [10] | GPIO 15    |
GPIO17|[11] [12] | GPIO 18    |
GPIO27|[13] [14] | GND        |
GPIO22|[15] [16] | GPIO 23    |
 3.3V |[17] [18] | GPIO 24    |
MOSI10|[19] [20] | GND        |
MISO 9|[21] [22] | GPIO 25    |
 SCLK |[23] [24] | CE0        |
 GND  |[25] [26] | CE1        |
...   |     ...   | ...        |
```
- See [pinout.xyz](https://pinout.xyz/) for a full graphical map.

---

## Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/jeffep/pi-sensor-suite.git
   cd pi-sensor-suite
   ```

2. **Install dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-picamera
   pip3 install -r requirements.txt
   ```

3. **Enable interfaces (if needed):**  
   Run `sudo raspi-config` and enable:
   - I2C
   - 1-Wire
   - SPI
   - Camera

4. **Edit scripts if necessary** for GPIO pin numbers, topic names, or MQTT broker address.

---

## Running

```bash
bash run_all_sensors.sh
```
Each sensor script runs in the background and publishes MQTT messages to `pi/sensors/<sensor>`.

---

## MQTT Broker Configuration

- **Host:** 192.168.87.99 (`jarvis`)
- **Port:** 1883 (default)
- **Topic prefix:** `pi/sensors/`

---

## File Overview

- `scripts/bmp280.py` – BMP280 sensor MQTT publisher
- `scripts/bme280.py` – BME280 sensor MQTT publisher
- `scripts/mq135.py` – MQ-135 air quality sensor via MCP3008
- `scripts/mcp3008.py` – MCP3008 ADC controller
- `scripts/ds18b20.py` – DS18B20 temperature publisher
- `scripts/hc_sr501.py` – HC-SR501 motion sensor & camera trigger
- `run_all_sensors.sh` – Starts all sensor publishers

---

## License

MIT License

---

## References

- [pinout.xyz](https://pinout.xyz/) for full Raspberry Pi pinout
- [Adafruit BMP/BME280 Python Libraries](https://github.com/adafruit/Adafruit_Python_BMP)
- [Adafruit MCP3008 Python Library](https://github.com/adafruit/Adafruit_Python_MCP3008)
- [w1thermsensor](https://github.com/timofurrer/w1thermsensor)
- [paho-mqtt](https://pypi.org/project/paho-mqtt/)
````
