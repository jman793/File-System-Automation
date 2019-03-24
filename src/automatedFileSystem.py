from Tkinter import *
import os,tkFileDialog
#Change this name to what you want the flags file to be set to
flagFileName='flags.txt'
#This character determines how the file path will actually be saved
#If you do not want a delimitter than change the value to ''
delimitingChar=':'
map={}
mainWindow=Tk()
frame=Frame(master=mainWindow,width=500,height=500)
frame.pack()


class ButtonFormat:

    def __init__(self,str):
        self.b=Button(master=frame,text=str,command=self.buttonHandle)
        self.b.pack(fill=BOTH,expand=1)
        self.b.pack_propagate(0)

    def buttonHandle(self):
        fileBrowswer=tkFileDialog.asksaveasfile(initialdir=map[self.b['text']],mode="w+")




def readInput():
    lines=[]
    flags=[]
    f=open(flagFileName)
    for x in f:
        lines.append(x.split(delimitingChar,1)[-1])
        flags.append(x.split(' ',1)[0])
    for i in range(len(lines)):
        lines[i]=lines[i].split('\n',1)[0]
    for i in range(len(lines)):
        map[flags[i]]=lines[i]
    setupUI()

def setupUI():
    label=Label(master=frame,text='Where would you like the file to go?')
    label.pack()
    for x in map.keys():
        myButtonFormat=ButtonFormat(x)
    doneButton=Button(master=frame,text='Done',command=done)
    doneButton.pack()

def done():
    mainWindow.destroy()

readInput()
mainWindow.mainloop()
