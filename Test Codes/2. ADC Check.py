from machine import Pin, ADC
from utime import sleep_ms

rj = Pin('LED', Pin.OUT)
volt = ADC(0)

while(True):
    rj.toggle()
    sleep_ms(50)
    print(volt.read_u16())
    sleep_ms(50)

