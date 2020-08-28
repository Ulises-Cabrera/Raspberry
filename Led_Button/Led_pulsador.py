import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

while True:
    if GPIO.input(3):
        GPIO.output(12,False)
    else:
        GPIO.output(12,True)
    
