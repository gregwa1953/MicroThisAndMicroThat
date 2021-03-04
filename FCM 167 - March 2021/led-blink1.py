 Micro This And Micro That - FCM #167
# ======================================
# For use on the Raspberry Pi Pico
# --------------------------------------
# LED Blink
# imports
import machine
import utime
led_onboard = machine.Pin(25,machine.Pin.OUT)
while True:
    led_onboard.value(1)
    utime.sleep(3)
    led_onboard.value(0)
    utime.sleep(3)

