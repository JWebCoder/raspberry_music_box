from gpiozero import Button
import subprocess
import time

resetSwitch = Button(pin = 26, hold_time=0.1)

def onPressReset(button):
  subprocess.run(["service", "soundbox", "restart"]) 

resetSwitch.when_held = onPressReset

while (True):
  time.sleep(10)
