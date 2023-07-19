try:
    import subprocess
    from pyroblox import *
    from storage.filesys.file import *
except ImportError:
    print("Could not import libraries.")

readFileData("storage/settings")

method = lineData[0]
imgres = lineData[9]
vip = lineData[8]
allCSPx = []
allCSPy = []
lastPixel = (0,0,0)

# Chat.say("!shout PaintBot Started Drawing.")

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
for i in range(imglen):
  for i in range(imgwid):
    pass