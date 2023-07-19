try:
 import keyboard
 import time
 import pygetwindow as gw
except ImportError:
 print("Could not import libraries, pyroblox is quitting.")
 exit()

ROBLOXINSTANCE = gw.getWindowsWithTitle("Roblox")[0]

class Window:
 def focus():
  ROBLOXINSTANCE.activate()

class Chat:
 def say(message):
  Window.focus()
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")
  keyboard.press("/") 
  time.sleep(0.01)
  keyboard.release("/")
  keyboard.write(message,0.005)
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")