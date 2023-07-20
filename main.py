try:
    import numpy as np
    import subprocess
    import sys
    import keyboard
    import time
    from PIL import Image
    from storage.pyroblox.pyroblox import Chat, Window
    from storage.filesys.file import *
    from storage.cf.find import *
except ImportError:
    print("Could not import libraries.")

method = sys.argv[1]
imgres = sys.argv[2]
vip = sys.argv[3]
image = sys.argv[4]

image = Image.open(image).convert("RGB")
real_image = np.array(image)
nearest_colors = find_nearest_colors(real_image, limited_colors)

readFileData()

keyboard.press("shift")
time.sleep(0.2)
keyboard.release("shift")
Window.click(960,960)
Chat.say("!shout PaintBot Started Drawing.")
def vk2di(mode):
 if mode == "open":
  subprocess.call(["C:\Program Files\AutoHotkey\AutoHotkey.exe", "storage/vk2di.ahk"])
 elif mode == "close":
  raise NotImplementedError
# CSP Calculator

if vip == "True":
   print("CSP Calculator Skipped")
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

# Pixel Calculator

imglen, imgwid, = imgres.split("x")
imglen = int(imglen)
imgwid = int(imgwid)

allPixelx = []
allPixely = []

for i in range(imglen):
  for i in range(imgwid):
    pass