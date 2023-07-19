try:
    import win32api, win32con
    import time
    import keyboard
    from pyroblox import *
    from storage.filesys.file import *
except ImportError:
    print("Could not import libraries.")

readFileData("storage/settings")

method = lineData[0]
imgres = lineData[9]
vip = lineData[8]
allCSP = []
lastPixel = (0,0,0)

def betterClick(x,y,delay=0.05):
    Window.focus()
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(delay)
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
    CSPgap = int(CSPgap)
    startingCSPx = int(startingCSPx)
    startingCSPy = int(startingCSPy)
    newCSPy = startingCSPy
    newCSPx = startingCSPx
    for i in range(18):
     newCSPy += CSPgap*i
     for i in range(8):
      newCSPx += CSPgap*i
      allCSP.append((newCSPx, newCSPy))
      newCSPx = startingCSPx
     newCSPy = startingCSPy
    print(allCSP)