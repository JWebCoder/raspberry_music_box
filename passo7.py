from gpiozero import LED
from time import sleep
from sound_button import SoundButton

led = LED(17)

SoundButton(
  27,
  [
    "./audio_button1_1.wav"
  ]
)

while (True):
  led.on()
  sleep(1)
  led.off()
  sleep(1)
