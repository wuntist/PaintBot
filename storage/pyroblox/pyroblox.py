try:
 import keyboard
 import time
 import pygetwindow as gw
 import win32con, win32api
except ImportError:
 print("Could not import libraries, pyroblox is quitting.")
 exit()

ROBLOXINSTANCE = gw.getWindowsWithTitle("Roblox")[0]

class Window:
 def focus():
  ROBLOXINSTANCE.activate()
 def click(x,y,delay=0.05):
  Window.focus()
  win32api.SetCursorPos(x,y)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
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