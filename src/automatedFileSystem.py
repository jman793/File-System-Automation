from Tkinter import *
import os
#Change this name to what you want the flags file to be set to
flagFileName='flags.txt'
#This character determines how the file path will actually be saved
#If you do not want a delimitter than change the value to ''
delimitingChar=':'
lines=[]
flags=[]
loopcontrol=True
possibleInputs=['yes','no','Yes','No','Y','N','y','n']
yes=['yes','Yes','Y','y']
no=['no','No','N','n']
map={}
window=Tk()
frame=Frame(master=window,width=500,height=500)
frame.pack()


class ButtonFormat:

    def __init__(self,str):
        self.b=Button(master=frame,text=str,command=self.buttonHandle)
        self.b.pack(fill=BOTH,expand=1)
        self.b.pack_propagate(0)

    def buttonHandle(self):
        print self.b.cget('text')




def readInput():
    f=open(flagFileName)
    for x in f:
        lines.append(x.split(delimitingChar,1)[-1])
        flags.append(x.split(' ',1)[0])
    for i in range(len(lines)):
        lines[i]=lines[i].split('\n',1)[0]
    for i in range(len(lines)):
        map[flags[i]]=lines[i]
    setupUI()
#TODO
def setupUI():
    label=Label(master=frame,text='Where would you like the file to go?')
    label.pack()
    for x in flags:
        myButtonFormat=ButtonFormat(x)
    doneButton=Button(master=frame,text='Done',command=done)
    doneButton.pack()

def done():
    window.destroy()

#TODO reformat this to work with the UI
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
#while(window.winfo_exists()):
    #pass
