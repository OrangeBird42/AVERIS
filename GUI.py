
from tkinter import *
import tkinter.messagebox
from VideoFinder import *
root = Tk()
import urllib.request
import urllib.parse
import re
import urllib
from VideoDownloader import *
import time
from VideoPlayer import *

textBox = Entry(root, width=50)
textBox.pack()

class Window(Frame): #defines window hahahahh
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        
        exitButton.place(x=0, y=0)

        clearButton = Button(self, text="Clear", command=self.clickClearButton)
        
        clearButton.place(x=0, y=20)

        helloButton = Button(self, text="What would you like to learn?", command=self.clickHelloButton)

        helloButton.place(x=42, y=57)

    


    def clickExitButton(self):
        exit()

    def clickHelloButton(self): 
        search_query = textBox.get()
        Finder(search_query)
        time.sleep(0.7)
        return Downloader()
        time.sleep(7) 
        #return Player()
        self.LoadingScreen
    
    def clickClearButton(self):
        return Clear()
         
def loading_screen(self):
        loading_screen = Toplevel(root)
        loading_screen.title("Loading Screen")
        loading_screen.geometry("200x200")
        label = Label(loading_screen, text="This is a loading screen")
        label.pack()
        

app = Window(root)
root.wm_title("AVERIS") #names the window
root.geometry("320x200")
root.mainloop()