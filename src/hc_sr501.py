import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
from picamera import PiCamera

MQTT_BROKER = '192.168.87.99'
MQTT_TOPIC = 'pi/sensors/motion'
PIR_PIN = 17  # Change as needed
CAMERA_IMAGE_PATH = '/tmp/motion.jpg'

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    camera = PiCamera()
    print("PIR sensor initialized. Waiting for motion...")
    try:
        while True:
            if GPIO.input(PIR_PIN):
                print("Motion detected!")
                camera.capture(CAMERA_IMAGE_PATH)
                payload = '{"motion": true}'
                client.publish(MQTT_TOPIC, payload)
                # Optionally, add code to send the image or notify
                time.sleep(5)  # Prevent multiple triggers
            else:
                time.sleep(0.1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
