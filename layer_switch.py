from gpiozero import Button

"""
00 - 0
01 - 1
10 - 2
11 - 3
"""

class LayerSwitch:
  def __init__(self):
    self.soundSwitchOne = Button(pin = 13)
    self.soundSwitchTwo = Button(pin = 6)

  def getActiveLayer(self):
    if (self.soundSwitchOne.is_active):
      if (self.soundSwitchTwo.is_active):
        return 3
      return 2
    if (self.soundSwitchTwo.is_active):
      return 1
    return 0
