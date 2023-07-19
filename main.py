try:
    from pyroblox.pyroblox import Chat, Window
    from pyroblox.pyroblox import *
    import win32api, win32con
    import time
    import keyboard
    from filesys.file import *
except ImportError:
    print("Could not import libraries.")

readFileData("settings")

startingCSPx = lineData[3]
startingCSPy = lineData[4]
CSPwidth = 8
CSPlength = 16
CSPgap = lineData[2]
allCSP = []
lastPixel = (0,0,0)

def betterClick(x,y):
    Window.focus()
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

Chat.say("!shout PaintBot Started Drawing.")

# CSP Calculator

for i in range(CSPlength):
 for i in range(CSPwidth):
  i = i + 1
  newCSPx = startingCSPx + CSPgap*i
 i = i + 1
 newCSPy = startingCSPy + CSPgap*i
 allCSP.append((startingCSPx, startingCSPy))
print(allCSP)

while keyboard.is_pressed('q') == False:
 for i in allCSP:
  print(i)
  print(allCSP[i])
  betterClick(allCSP[i])