import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Pin configuration

LED_PIN =4 # Replace with the GPIO pin connected to the push-button (SW pin)

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Enable internal pull-up resistor

GPIO.output(LED_PIN,GPIO.HIGH) #led on
time.sleep(1)
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(2)
GPIO.cleanup()  # Clean up the GPIO configuration before exiting

