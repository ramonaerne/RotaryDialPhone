from gpiozero import Button
from signal import pause
from time import sleep

count = 0

def say_hello():
    global count
    count = count + 1
#    print("count: ", count)

def hooked(inp):
    global count
    sleep(0.1)
    print("hooked on count: ", count)
    count = 0

def hooked_p():
    count = 0
    print("hooked pressed")

button = Button(17)
hook = Button(18)

button.when_pressed = say_hello
hook.when_released = hooked
hook.when_pressed = hooked_p
pause()
