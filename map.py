from tkinter import *

root = Tk()
root.title('map heare we go......')


img = PhotoImage(file='images/h.png')

Label(
    root,
    image=img
).pack()

btn1 = Button(text="back",command=quit)
btn1.pack()

root.mainloop()