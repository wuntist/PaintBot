try:
 import keyboard
 import time
 import pygetwindow as gw
 import win32con, win32api
 import pydirectinput
except ImportError:
 print(f"Could not import libraries, pyroblox is quitting.")
 exit()

try:
 ROBLOXINSTANCE = gw.getWindowsWithTitle("Roblox")[0]
except IndexError:
 print(f"Roblox not found, pyroblox is quitting.")
 RoID = 1

class Window:
 def focus():
  ROBLOXINSTANCE.activate()
 def click(x,y,delay=0.04):
  Window.focus()
  win32api.SetCursorPos(x,y)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  pydirectinput.moveTo(x,y)
  time.sleep(delay)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
class Chat:
 def say(message):
  Window.focus()
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")
  keyboard.press("/") 
  time.sleep(0.01)
  keyboard.release("/")
  keyboard.write(message,0.025)
  keyboard.press("\n")
  time.sleep(0.01)
  keyboard.release("\n")