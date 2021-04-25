#Clase Arista
class Arista:
  def __init__(self, source, target):
    self.source = source
    self.target = target
    self.id = str(source)+' -> '+str(target)
  def __str__(self):
    return str(self.id)
#******************************************************************************
