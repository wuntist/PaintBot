lineData = []

def readFileData(file):
    with open(file,'r') as f:
            for line in f.readlines():
                lineData.append(line.rstrip())

def printFileData():
    for line in lineData:
        print(line)

def addFileData(file,data):
    with open(file,'a') as f:
        f.write(data + "\n")