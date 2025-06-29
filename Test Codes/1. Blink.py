from machine import Pin
from utime import sleep_ms


rj = Pin('LED', Pin.OUT)

while(True):
    rj.toggle()
    sleep_ms(5000)