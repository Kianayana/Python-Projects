import tkinter as tk
from tkinter import *
import webbrowser

#This will create a pop-up window that allows us to open up the index for our website
class ParentWindow(Frame):
    def __init__(self, master):
        #This creates the frame for the window
        Frame.__init__(self, master)
        #This adds text to the title bar of the window
        self.master.title("Web Page Generator")
        #This allows me to add text directly onto the frame itself
        self.txt = Label(text="Enter custom text or click the Default HTML page button")
        self.txt.grid(row=0, padx=(10,10), pady=(10,10), sticky=W)
        #This creates an entry line for the use to input text that can show on the website
        self.source_dir = Entry(width=125)
        self.source_dir.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,0))
        #This creates a button that produces the default text we set through defaultHTML
        self.html_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.html_btn.grid(row=2, column=0, padx=(300,0) , pady=(10,10))
        #This creates a button that produces the text we set through defaultHTML
        self.custom_btn =Button(self.master, text="Submit Custom Text", width=30, height=2,command=self.customText)
        self.custom_btn.grid(row=2, column=1, padx=(0,10) , pady=(10,10))
        
       
    #This function controls the display of the default text on the website
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        #this closes the function when it is done
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    #this function controls the display of the entry on the website
    def customText(self):
        #this line allows us to use the customer text that was input into the entry
        c_input=self.source_dir.get()
        c_file = open("index.html", "w")
        c_file.write(c_input)
        #this closes the function when it is done
        c_file.close()
        webbrowser.open_new_tab("index.html")
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
