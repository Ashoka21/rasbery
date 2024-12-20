import RPi.GPIO as GPIO
import time
 
# Pin configuration
BUTTON_PIN =4 # Replace with the GPIO pin connected to the push-button (SW pin)
 
# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Enable internal pull-up resistor
 
# Function to handle button press
def button_callback(channel):
   
        print("Button Pressed!")
   
try:
    
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=200)
    print("waiting to button press")
    while True:
        time.sleep(0.1)  # Keep the program running
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    GPIO.cleanup()  # Clean up the GPIO configuration before exiting
