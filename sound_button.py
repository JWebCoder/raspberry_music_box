from sound_file import Sound
from gpiozero import Button

class MockLayerSwitch:
  def getActiveLayer():
    return 0

class SoundButton:
  def __init__(self, pin, sounds, layerSwitch = MockLayerSwitch()):
    self.layerSwitch = layerSwitch
    self.pin = pin
    self.sounds = []
    self.button = Button(pin = pin, hold_time=0.01)
    self.button.when_held = self._onHeld
    self.button.when_released = self._onRelease
    for path in sounds:
      self.sounds.append(Sound(path))
  
  def _onHeld(self, button):
    self._playSound(self.layerSwitch.getActiveLayer())
  
  def _onRelease(self, button):
    print((f"audio {self.layerSwitch.getActiveLayer()} GPIO {self.pin}") )
  
  def _playSound(self, activeLayer):
    if activeLayer < len(self.sounds) and self.sounds[activeLayer] != "":
      try:
        self.sounds[activeLayer].parsedSound.play()
      except:
        self.sounds[activeLayer].parseSound()
    return
