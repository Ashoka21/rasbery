import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define pins for rotary switch
ROTARY_PINS = [0,]

# Setup GPIO input with pull-down resistors
for pin in ROTARY_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Rotary Switch Active Position Detection\nPress Ctrl+C to exit.\n")
    
    while True:
        active_position = None
        for position, pin in enumerate(ROTARY_PINS, start=1):
            if GPIO.input(pin) == GPIO.HIGH:
                active_position = position
                break
        
        if active_position:
            print(f"Active Position: {active_position}")
        else:
            print("No Active Position Detected")
        
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nProgram terminated.")
finally:
    GPIO.cleanup()
