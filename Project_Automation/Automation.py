def open_school():
    pass
def open_coding():
    pass
def open_play():
    pass
def open_watch():
    pass

from tkinter import *
root=Tk()
root.title("Automation")
root.geometry("250x250")
root.iconbitmap('Papirus-Team-Papirus-Apps-Python.ico')
root.configure(bg="green")
frame=Frame(root)
ButtonC=Button(frame,text="Coding",command=open_coding,height=2,width=10,font=("Calibri"),bg="blue")
ButtonS=Button(frame,text="School",command=open_school,height=2,width=10,font=("Calibri"),bg="blue")
ButtonP=Button(frame,text="Play",command=open_play,height=2,width=10,font=("Calibri"),bg="blue")
ButtonW=Button(frame,text="Watch",command=open_school,height=2,width=10,font=("Calibri"),bg="blue")
ButtonC.pack()
ButtonS.pack()
ButtonP.pack()
ButtonW.pack()
frame.pack(expand=YES)
root.mainloop()