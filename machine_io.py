#Will only support stdio for now
import sys,os
from machine_define import *
from termcolor import colored, cprint
from machine_broadcast import Broadcast
rows, columns = os.popen('stty size', 'r').read().split()
def stdout(message):
  print message,
  print '\b' * len(message),   # \b: non-deleting backspace
def display(msg):
  if(isinstance(msg, Broadcast)):
    current_level=level_refrence[msg.level]
    level_text="["+current_level.nick+"]"
    if current_level.color_p2=="":
      level_text=colored(level_text,current_level.color,attrs=current_level.attrs)
    else:
      level_text=colored(level_text,current_level.color,current_level.color_p2,attrs=current_level.attrs)
    body_text="["+str(msg.time)+"]:"+msg.message
    stdout(level_text.rjust(int(columns)))
    stdout(body_text)
    print
