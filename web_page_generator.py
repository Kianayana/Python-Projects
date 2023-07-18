import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.txt = Label(text="Enter custom text or click the Default HTML page button")
        self.txt.grid(row=0, padx=(10,10), pady=(10,10), sticky=W)
        
        self.source_dir = Entry(width=125)
        self.source_dir.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(10,0))

        self.html_btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.html_btn.grid(row=2, column=0, padx=(300,0) , pady=(10,10))

        self.custom_btn =Button(self.master, text="Submit Custom Text", width=30, height=2,command=self.customText)
        self.custom_btn.grid(row=2, column=1, padx=(0,10) , pady=(10,10))


        
       

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        c_input=self.source_dir.get()
        c_file = open("index.html", "w")
        c_file.write(c_input)
        c_file.close()
        webbrowser.open_new_tab("index.html")
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
