#Will only support stdio for now
from machine_define import *
def print_msg(msg):
  print "["+level_refrence[msg.level]+"]:"+msg.message