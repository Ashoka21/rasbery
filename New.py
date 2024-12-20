import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Pin configuration
BUTTON_PIN=26
LED_PIN =4 # Replace with the GPIO pin connected to the push-button (SW pin)

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Enable internal pull-up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)
DEBOUNCE_TIME=0.2
try:
    
    while True:
        if GPIO.input(BUTTON_PIN)==GPIO.LOW:
            GPIO.output(LED_PIN,GPIO. HIGH) #led on
            print("button pressed led on")
            time.sleep(DEBOUNCE_TIME)
        else:
         GPIO.output(LED_PIN, GPIO.LOW)
         print("button not pressed led off")
        time.sleep(0.01)
    
except KeyboardInterrupt:
   
    print("Exiting program.")
finally:
    GPIO.cleanup()  # Clean up the GPIO configuration before exiting

