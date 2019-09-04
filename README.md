# Pycom LoPy LORA range checker

A Python script for the Pycom LoPy to check if TTN LORA is present at the current location. I used this script in the car to see how far my TTN gateway ranges and to see where TTN LORA gateways are present while driving in the car. 

Color codes:
- On boot the lopy led flashes Red, Green, Blue
- If LoPy flashes Red, no TTN LORA gateway is reachable
- If LoPy flashes Green, a LORA message was sent succesfully
