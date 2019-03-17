import os
#Change this name to what you want the flags file to be set to
flagFileName='flags.txt'
#This character determines how the file path will actually be saved
#If you do not want a delimitter than change the value to ''
delimitingChar=':'
lines=[]
flags=[]
possibleInputs=['yes','no','Yes','No','Y','N']
yes=['yes','Yes','Y']
no=['no','No','N']
map={}

def readInput():
    f=open(flagFileName)
    for x in f:
        lines.append(x.split(delimitingChar,1)[-1])
        flags.append(x.split(' ',1)[0])
    for i in range(len(lines)):
        lines[i]=lines[i].split('\n',1)[0]
    for i in range(len(lines)):
        map[flags[i]]=lines[i]

def userInput():
    print 'Where would you like this file to go?'
    for x in flags:
        print x
    path=raw_input()
    while path not in flags:
        print 'Error incorrect input, choose from list'
        path=raw_input()
    return path

def moveFiles(choice):
    path=map[choice]
    os.chdir(path)
    print 'Would you like to make a new folder for this addition?'
    input=raw_input()
    while input not in possibleInputs:
        print 'Error incorrect input, choose from list'
        input=raw_input()
    if input in yes:
        dirName=raw_input('What would you like the directory to be named?')
        os.mkdir(dirName)
        if raw_input('Would you like to add a file to this directory?') in no:
            return
    open(raw_input('What would you like to name the file? (add ext)'),"w+")


readInput()
moveFiles(userInput())
