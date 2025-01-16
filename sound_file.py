from fileParser import audioparser

class Sound:
  def __init__(self, path):
    self.path = path
    self.parseSound()

  def parseSound(self):
    if self.path:
      self.parsedSound = audioparser(self.path)
