import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
# Pin configuration
BUTTON_PIN=26


# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    
    while True:
        button_state=GPIO.input(BUTTON_PIN)
        print(f"button stae :{button_state}")
        time.sleep(1)
       
    
except KeyboardInterrupt:
   
    print("Exiting program.")
finally:
    GPIO.cleanup()  # Clean up the GPIO configuration before exiting
