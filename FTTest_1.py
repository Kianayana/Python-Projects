import tkinter as tk
from tkinter import *

import tkinter
import tkinter.filedialog
import os
import sys
import shutil
import time
import datetime
from datetime import datetime, timedelta

import schedule


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        #Sets title pf GUI window
        self.master.title("File Transfer")
        
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text = "Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Creates entry for destination directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid() padx and pady are the same ad
        #on he next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions destinations button in GUI using tkinter grid() padx and pady are the same as 
        #the buton to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))

        #Create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0,15))

        
    #Creates function to select source directory
    def sourceDir (self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be instered into the Entry widget properly
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    #Creates function to sleect destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clar the content that is inserted in the Entry widget,
        #this allows the path to be insered into the Entry widget properly.
        self.destination_dir.delete(0, END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets srouce directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)

        
        # START FILE TRANSFER PART THREE code
        #This section is to track the most recent updates to a file
        #Setting the source (path) and destination (destination2) to the two folders we want to check
        path = "C:/Users/kiana/Desktop/Customer Source/"
        destination2 = "C:/Users/kiana/Desktop/Customer Destination/"
        #Retreiving a list of files in the source directory
        fix1 = os.listdir(path)
        #trying to receive the time stamp of the files in the path, but I believe this is just looking at the last modification of the entire directory
        t_hours = os.path.getmtime(path)
        fl_fix = datetime.fromtimestamp(t_hours)
        #trying to convert fix1 into a string or integer that the timestamp or getmtime will recognize. Not sure how to do it
        l_hours = datetime.fromtimestamp(fix1)
        #creating a timedelta to subtract 24 hours/-86400 seconds from the timestamps of each file 
        delta = timedelta(seconds = -86400)
        #subtracting the time delta from the timestamps to get the result
        fix2 = fl_fix + delta
        #creating a statement that starts the transfer if 
        if l_hours < fix2:
            #comparing the if statement to each file in fix1. I don't think I'm doing this the correct way 
            for i in fix1:
                #moves each file from the source to the destination
                shutil.move(path + '/' + i, destination2)
                print(i + 'was successfully transferred.')
        #I'm also unsure whether to use import schedule to schedule this code to run once a day automatically
        #In order to do this, will I need path and destination2 to automatically fill the entry portion of program?
        #END FILE TRANSFER PART THREE code

               
            

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

   


        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
    

