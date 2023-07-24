try:
    import numpy as np
    import subprocess
    import sys
    import keyboard
    import time
    from PIL import Image
    from storage.pyroblox.pyroblox import Chat, Window
    from storage.pyroblox.pyroblox import *
    from storage.filesys.file import *
except ImportError:
    print("Could not import libraries.")

method = sys.argv[1]
vip = sys.argv[2]
sc_res = sys.argv[3]
scrlen, scrwid, = sc_res.split("x")
srclen = int(scrlen)
scrwid = int(scrwid)

readFileData()

if RoID == 0:
  keyboard.press("shift")
  time.sleep(0.2)
  keyboard.release("shift")
  Window.click(960,960)
  Chat.say("!shout PaintBot Started Drawing.")
  subprocess.call(["C:\Program Files\AutoHotkey\AutoHotkey.exe", "storage/vk2di.ahk"])
else:
  print("Roblox not found")


if method == "blockatepaint":
    if vip == "True":
      pass
    else:
      if vip == "False":
        allCSPx = []
        allCSPy = []
        CSPgap = lineData[2]
        startingCSPx = lineData[3]
        startingCSPy = lineData[4]
        CSPgap = int(CSPgap)
        startingCSPx = int(startingCSPx)
        startingCSPy = int(startingCSPy)
        newCSPy = startingCSPy
        newCSPx = startingCSPx
        for i in range(16):
         newCSPy += CSPgap*i
         newCSPy = startingCSPy
         for i in range(8):
          newCSPx += CSPgap*i
          newCSPx = startingCSPx
          allCSPx.append(newCSPx)
        allCSPy.append(newCSPy)
        print(allCSPx, allCSPy)
    allPixelx = []
    allPixely = []
    for i in range(scrlen):
      for i in range(scrwid):
        raise NotImplementedError
elif method == "robloxpaint":
   raise NotImplementedError