import pydirectinput as gui
from time import sleep
import random


counter = 20
sleep(5)

while counter > 0:
    gui.press("e")
    sleep(random.randint(1, 2))
    gui.click(x=2172 , y=1811)




print(gui.position())
