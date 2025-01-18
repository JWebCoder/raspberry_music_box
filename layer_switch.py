from gpiozero import Button

"""
00 - 0
01 - 1
10 - 2
11 - 3
"""

class LayerSwitch:
  def __init__(self):
    self.layer = 0
    self.soundSwitch = Button(pin = 13, hold_time=0.01)
    self.soundSwitch.when_held = self._onHeld
  
  def _onHeld(self, button):
    if self.layer == 3:
      self.layer = -1
    self.layer += 1
  
  def getActiveLayer(self):
    return self.layer
