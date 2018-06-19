# File: assignment12.py
# Name: Carole (Chia Jung) Sung
# Date: April 26 2018
# Description: Chapter 13 programming exercise 1, 
#2 (but use Radio Buttons for each word), 3 and 6

import tkinter


class MyGui:
    def __init__(self):
        #Create main window widget.
        self.main_window = tkinter.Tk()

        #Create two frames, one for the top of the window
        #and one for the bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        self.top_frame.pack()
        self.bot_frame.pack()
        
        #Create buttons
        self.showInfoBtn = tkinter.Button(self.bot_frame, text="Show Info", command=self.showInfo)
        self.quitBtn = tkinter.Button(self.bot_frame, text="Quit",command=self.main_window.destroy)

        #Pack Buttons
        self.showInfoBtn.pack(side="left")
        self.quitBtn.pack(side="left")

        #Enter the tkinter main loop.
        tkinter.mainloop()

    def showInfo(self):
        #Display info dialog 
        #Create label widget
        self.label1 = tkinter.Label(self.top_frame, text="Steven Marcus")
        self.label2 = tkinter.Label(self.top_frame, text="274 Baily Drive")
        self.label3 = tkinter.Label(self.top_frame, text="Waynesville, NC 27999")
        
        #Call the Label widget's pack method.
        self.label1.pack(side="top")
        self.label2.pack(side="top")
        self.label3.pack(side="top")

my_gui=MyGui()

