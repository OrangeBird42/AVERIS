
from tkinter import *
import tkinter.messagebox
from VideoFinder import Finder
root = Tk()
import urllib.request
import urllib.parse
import re
import urllib


textBox = Entry(root, width=50)
textBox.pack()

class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        exitButton.place(x=0, y=0)

        helloButton = Button(self, text="What would you like to learn?", command=self.clickHelloButton)

        helloButton.place(x=42, y=57)


    def clickExitButton(self):
        exit()

    def clickHelloButton(self): 
        search_query = textBox.get()
        Finder(search_query)
         
         #Answer = Label(root, text = textBox.get())
         #Answer.pack()
         #return Finder(Answer)
        
        

app = Window(root)
root.wm_title("Tkinter window") #names the window
root.geometry("320x200")
root.mainloop()