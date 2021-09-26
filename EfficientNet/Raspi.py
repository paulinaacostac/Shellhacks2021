# for Raspi commands
# import RPi.GPIO as GPIO 
# from gpiozero import LED
# from gpiozero.pins.pigpio import PiGPIOFactory as GPIO
# from time import sleep

# left = 17
# # right = 27
# GPIO.setmode(GPIO.BCM)
# factory = GPIO(host='192.168.4.1') #http://192.168.4.1:8081/video_feed
# # led = LED(17, pin_factory = factory)

# def low_vibration(num):    
#     GPIO.setup(num, GPIO.OUT)
#     print ("PIN on: ", num)
#     GPIO.output(num, GPIO.HIGH) 
#     sleep(1)
#     print ("PIN off: ", num)
#     GPIO.output(num,GPIO.LOW)

# def high_vibration(num):
#     GPIO.setup(num, GPIO.OUT)
#     print ("PIN on: ", num)
#     GPIO.output(num, GPIO.HIGH)
#     sleep(1)
#     print ("PIN off: ", num)
#     GPIO.output(num,GPIO.LOW)

# # def both_sensors():
# #     GPIO.setup(left, GPIO.OUT)
# #     GPIO.setup(right, GPIO.OUT)
# #     print ("PINS on: ", left, right) 
# #     GPIO.output(left, GPIO.HIGH)
# #     GPIO.output(right, GPIO.HIGH)
# #     sleep(1)
# #     print ("PINs off: ", left, right)
# #     stop_vibration()

# def stop_vibration():
#     GPIO.output(left,GPIO.LOW)
#     # GPIO.output(right,GPIO.LOW)

# high_vibration(left)
# # low_vibration(right)
# stop_vibration()
# # both_sensors()


from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.4.1')
right_heptic = LED(17, pin_factory=factory)
left_heptic = LED(27, pin_factory=factory)

for i in range(5):
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)