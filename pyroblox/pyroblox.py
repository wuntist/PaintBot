"""Custom python library by wuntist to manipulate in-game events."""

# TODO:
# - Setup a chat send and read api (python). (NOT POSSIBLE FOR NOW)
# - More manipulation features. (Character and Window)
# - Savestates and macros. (Repeat, Said, Toggle)
# - QoL stuff.


# Importing libraries.

try:
 import keyboard
 import time
 import pygetwindow as gw
except ImportError:
 print("Could not import libraries, pyroblox is quitting.")
 exit()

# Setting up variables & constants.

ROBLOXINSTANCE = gw.getWindowsWithTitle("Roblox")[0]

# Setting up the functions & classes.

class Window:
 def focus():
  ROBLOXINSTANCE.activate()

class Chat:
 def say(message):
  """"Says something inside of the chat using advanced techniques (Please tell me if there are better methods)"""
  SaidText = message
  Window.focus()
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")
  keyboard.press("/") 
  time.sleep(0.01)
  keyboard.release("/")
  keyboard.write(message)
  time.sleep(0.25)
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")