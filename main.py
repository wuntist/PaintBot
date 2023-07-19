try:
    from pyroblox import *
    import win32api, win32con
    import time
    import keyboard
    from filesys.file import *
except ImportError:
    print("Could not import libraries.")

readFileData("settingsHolder/settings")

method = lineData[0]
print(method)
imgres = lineData[9]
vip = lineData[8]
allCSP = []
lastPixel = (0,0,0)

def betterClick(x,y):
    Window.focus()
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Chat.say("!shout PaintBot Started Drawing.")

# CSP Calculator

if vip == "True":
   print("CSP Calculator Skipped")
else:
  if vip == "False":
    CSPgap = lineData[2]
    startingCSPx = lineData[3]
    startingCSPy = lineData[4]
    int(CSPgap)
    int(startingCSPx)
    int(startingCSPy)
    for i in range(18):
     newCSPy =+ startingCSPy
     for i in range(8):
      newCSPx =+ startingCSPx
     allCSP.append((newCSPx, newCSPy))
    print(allCSP)