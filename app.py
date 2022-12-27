
import os
import subprocess
import sys
import tkinter as tk
from lib2to3.pgen2.token import NEWLINE
from tabnanny import filename_only
from tkinter import Text, filedialog

root = tk.Tk()
apps = []


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        apps = tempApps.split(',')
       # apps = [x for x in tempApps if x.strip()]


def addApp():

    for  widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir='/',title='Select File',
    filetypes=(('executables','*.app'),('all files',"*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,bg='#263D42')
        label.pack()
def runApps():
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])


canvas = tk.Canvas(root, height=700, width=700,bg='#263D42')
canvas.pack()

frame = tk.Frame(root,bg='white')
frame.place(relwidth=0.8,relheight=0.8,relx=0.1)
openFile=tk.Button(root, text='Open File', padx=10,pady=5,fg='white',bg='#263D42', command=addApp)
openFile.pack()

runApps = tk.Button(root,text='Run App ', padx=10,pady=5,fg='white',bg='#263D42',command = runApps)
runApps.pack()

for app in apps: 
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()


with open('save.txt','w') as f:
    for app in apps:
       f.write(app+','+'\n')
       

 