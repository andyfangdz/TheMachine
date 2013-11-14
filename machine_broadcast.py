import machine_io
class Broadcast:
  def __init__(self,_level=0,text=""):
    self.level=_level
    self.message=text
  def display(self):
    machine_io.print_msg(self)