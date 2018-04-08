#Created by Samuel Phillips!
import tkinter
import playsound
from tkinter import *
from playsound import playsound

#Create the window

window = Tk()
window.geometry("500x200")
window.title("easy-mp3-player")
window.resizable(width=False, height=False)
window.mainloop() 

#Add file playing methods

def callback():
    playsound("MUSICFILE.mp3")
    
#Add button


b = Button(text="Play", command = callback)
b.pack(side="top")
mainloop()
