from tkinter import *   #importing library for tkinter window
import os
import tkinter as tk

root=Tk()



root.geometry("647x415")  #giving geometry for tkinter window

def send():    #giving and taking commands from bot using if and elif and else condition
    
    f=e.get()
  #  print(f)
    z= f.lower()
   # print(z)
 
    send="you=>"+e.get()
    txt.insert(END,"\n"+send)
    
    Bot="Bot==>"
    
    if(z=="hello"):
        
        txt.insert(END,"\n"+"Bot=>hello")
        
    elif(z=="hi"):

        txt.insert(END,"\n"+"Bot=>hi")
        
    elif(z=="hi!,how are you?"):
        
        txt.insert(END,"\n"+"Bot=>fine and what about you?")
    
    elif(z==""):
        
        txt.insert(END,"\n"+Bot+"Enter Message.........!")
        
    
    
    elif(z=="can i get the map"):
        
        txt.insert(END,"\n"+Bot+"Yupe!!!!!!!")
        open2 = "map.py"
        os.system(open2)
    
        
    elif(z=="bye"):
        
        txt.insert(END,"\n"+Bot+"Ok Have A Nice Day!")
        root.destroy()
    else:
        txt.insert(END,"\n"+"Bot==>Sorry I don't Understand! Go to about Page And Contact Dev")
        
        open1= "about.py"
        os.system(open1)
        
    
    e.delete(0,END)
    
    
txt=Text()

txt.grid(row=0,column=0,columnspan=2)
#txt.config(state='disabled')

e=Entry(root,width=95,fg="green")#entry Box

e.grid(row=1,column=0) #position of entry box



click_btn= PhotoImage(file='images/s2.png')
img_label= Label(image=click_btn)

send=Button(root,text="send",width=55,height=19,command=send,image=click_btn,fg="green")  #send button
send.grid(row=1,column=1) #position of send button



btnx = Button(root,text="exit",command=exit)


root.title("Feel Free To Ask")    #name of window


#root.iconbitmap(r') #icon for tkinter window
p1 = PhotoImage(file = 'images\i1.png')
# Icon set for program window
root.iconphoto(False, p1)

root.mainloop()  #end of main loop