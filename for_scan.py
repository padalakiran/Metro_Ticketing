from tkinter import *
import os



root = Tk()
root.geometry("500x281")

#adding icon to tkinter

p1 = PhotoImage(file = f'images/ic.png')
root.iconphoto(True, p1)
man =('Times',14) 

root.title("........PK_Metro Welcomes You........")

def entry():
    path = 'entry_gate.py'
    os.system(path)
    
def exit_gate():
    path = 'exit_gate.py'
    os.system(path)
def main_menu():
    root.destroy()

btnq =  Button(root,text="Entry Gate",bd='0',height= 2, width=15,command=entry,bg='Green',font=man,fg='white')
btnq.place(x=50,y=70)

btnq =  Button(root,text="Exit Gate",bd='0',height= 2, width=15,command=exit_gate,bg='Red',font=man,fg='white')
btnq.place(x=270,y=70)

btnq =  Button(root,text="Main Menu",bd='0',height= 2, width=15,command=main_menu,bg='orange',font=man,fg='white')
btnq.place(x=150,y=140)




root.mainloop()