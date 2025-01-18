from layer_switch import LayerSwitch
from sound_button import SoundButton
from time import sleep
from gpiozero import LED

layerSwitch = LayerSwitch()

SoundButton(
  3,
  [
    "./audio_button1_1.wav",
    "./audio_button1_2.wav",
    "./audio_button1_3.wav",
    ""
  ],
  layerSwitch
)

SoundButton(
  4,
  [
    "./audio_button2_1.wav",
    "./audio_button2_2.wav",
    "./audio_button2_3.wav",
    ""
  ],
  layerSwitch
)

SoundButton(
  17,
  [
    "",
    "",
    "./audio_button3_3.wav",
    ""
  ],
  layerSwitch
)

SoundButton(
  27,
  [
    "",
    "",
    "./audio_button4_3.wav",
    ""
  ],
  layerSwitch
)

SoundButton(
  22,
  [
    "",
    "",
    "./audio_button5_3.wav",
    ""
  ],
  layerSwitch
)

led = LED(20)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

print("started")
try:
  while (True):
    sleep(10)
except KeyboardInterrupt:
    print('Interrupted')
