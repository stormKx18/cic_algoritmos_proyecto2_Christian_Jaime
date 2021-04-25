#Clase Nodo
class Nodo:
  def __init__(self, id):
    self.id = id
    self.grado=0
  def __str__(self):
      return str(self.id)
  def __eq__(self, otroNodo):
      return self.id == otroNodo.id
#******************************************************************************
