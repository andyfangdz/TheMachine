from termcolor import colored, cprint
class Level:
  def __init__(self,nick,color,color_p2,attrs):
    self.color=color
    self.nick=nick
    self.color_p2=color_p2
    self.attrs=attrs
  def __repr__(self):
    return "Level()"
  def __str__(self):
    return self.nick
Irrelevant=Level("Irrelevant","green","",["bold"])
Relevant=Level("Relevant","red","",["bold"])
Critical=Level("Critical","red","on_white",["bold"])
Machine=Level("Machine","cyan","",["bold"])
level_refrence={
  0:Irrelevant,
  1:Relevant,
  2:Critical,
  3:Machine
}
refrence_level={v:k for k, v in level_refrence.items()}
#code from http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
