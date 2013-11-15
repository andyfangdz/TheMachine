from machine_define import *
import datetime
class Broadcast:
  def __init__(self,_level=0,text=""):
    self.level=_level
    self.message=text
    self.time= datetime.datetime.now()
  #def display(self):
  #  machine_io.print_msg(self)
  # Above method is marked as depreciated
  def __repr__(self):
    return "Broadcast()"
  def __str__(self):
    return "["+str(level_refrence[self.level])+"]:"+self.message