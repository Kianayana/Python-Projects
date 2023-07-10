import sqlite3


conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    #Creating my table to show the files in my first folder
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_folder1(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)")
    conn.commit()
conn.close()


#accessing the files database again to add strings to it
conn = sqlite3.connect('files.db')

# tuple of files
fileList = ('information.docx', 'Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoro.jpg')

#this portion will allow me to see only text files
for txt in fileList:
    if txt.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row is the list in fileList
            cur.execute("INSERT INTO tbl_folder1 (col_filename) VALUES (?)", (txt,))
            print(txt)
conn.close()
            
