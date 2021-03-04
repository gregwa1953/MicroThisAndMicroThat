# Micro This And Micro That - FCM #167
# ======================================
# For use on the Raspberry Pi Pico
# --------------------------------------
# LED Throb 1
# Imports
from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(25))

pwm.freq(1000)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025,0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)
    sleep(0.8)
