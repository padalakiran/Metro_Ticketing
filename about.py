from tkinter import *
import webbrowser

root = Tk()
root.title('About Developer')
root.geometry('500x500')


new = 1
url = "https://padalakiran.wixsite.com/kiran-portfolio"

def openbrowser():
    webbrowser.open(url,new=new)

bg = PhotoImage(file = 'images/mts.png')

canvas = Canvas(
	root, 
	width = 500,
	height = 400
	)

canvas.pack(fill='both', expand = True)

canvas.create_image(
	0, 
	0, 
	image=bg,
	anchor = "nw"
	)


btn = Button(
	root, 
	text = 'EXPLORE MORE ABOUT DEVELOPER',
	command=openbrowser,
	width=35,
	height=2,
	#relief=SOLID,
	font=('arial', 12)
	)

btn_canvas = canvas.create_window(
	120, 
	200,
	anchor = "nw",
	window = btn,
	)


root.mainloop()