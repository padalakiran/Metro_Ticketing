from email.mime import message
from tkinter import*
import os
from tkinter import messagebox
import qrcode
import string   
import secrets 
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=" my sql password",
        database="dtabase name"
)

    mycursor = mydb.cursor()




    def complains():
        path = 'complaint.py'
        os.system(path)
        
        
    def for_login():
        path = 'login.py'
        os.system(path)

    def for_new_user():
        path = 'new_user.py'
        os.system(path)

    def for_map():
        path = 'map.py'
        os.system(path)

    def for_scan():
        path = 'for_scan.py'
        os.system(path)
    def Chat():
        path = 'quairy.py'
        os.system(path)
    # quairy.q()
    def about():
        path = 'about.py'
        os.system(path)
        
        
        
        
        
        
    #qr code generating
        
    def generate():
        res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.ascii_uppercase + string.ascii_lowercase) for x in range(20))  

        qr = qrcode.QRCode(version = 1,
                        box_size = 10,
                        border = 5)


        qr.add_data(res)

        qr.make(fit = True)
        img = qr.make_image()
        img.show('MyQRCode2.png')



        #print(res)
        try:
        
            sql="INSERT INTO tickets (Code,Entry_gate) VALUES (%s,%s);"
            val=(res,0)
            mycursor.execute(sql, val)
            mydb.commit()
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror("opps","Error Occured")

        



    root = Tk()
    root.geometry("500x281")

    #adding icon to tkinter

    p1 = PhotoImage(file = f'images/ic.png')
    root.iconphoto(True, p1)


    man =('Times',14) 

    # images
    bg = PhotoImage(file = 'images/e.png')
    my_la = Label(root,image = bg).place(x=0,y=0)



    #adding top menubars

    menubar = Menu(root, background='blue', fg='white')
    
    # Declare file and edit for showing in menubar
    file = Menu(menubar, tearoff=False, background='yellow')
    #edit = Menu(menubar, tearoff=False, background='pink')


    #menubar = Menu(root) 

    file = Menu(menubar, tearoff=0)  
    file.add_command(label="About",command=about)  
    file.add_command(label="Enquiry",command=Chat)   
    file.add_command(label="Raise a Complaint", command=complains)  
    file.add_command(label="Show Map", command=for_map)  
    

    file.add_separator()  
    file.add_command(label="Exit", command=root.destroy)

    menubar.add_cascade(label="☰Menu", menu=file)  


    edit = Menu(menubar, tearoff=0)  
    edit.add_command(label="Undo")  
    
    edit.add_separator()    


   




    


    root.config(menu=menubar)

    root.config(menu=menubar)

    #creating buttons


    btns =  Button(root,text="For qr",bd='0',height= 2, width=15,font=man,bg='orange',fg='white',command=generate)
    btns.place(x=50,y=50)

    #label1= Label(root,text="Generate qr Code",fg='orange').place(x=75,y=200)



    btnp =  Button(root,text="For scan",bd='0',height= 2, width=15,bg = 'Blue',fg='white',font =man, command=for_scan)
    btnp.place(x=255,y=50)

    #label2= Label(root,text="Scan qr Code",fg='blue').place(x=300,y=200)


    btnq =  Button(root,text="Exit",bd='0',height= 2, width=15,command=root.destroy,bg='red',font=man,fg='white')
    btnq.place(x=50,y=150)

    #label3= Label(root,text="Exit",fg='Red').place(x=225,y=325)


    btnq =  Button(root,text="Chat With Us",bd='0',height= 2, width=15,command=Chat,bg='Green',font=man,fg='white')
    btnq.place(x=255,y=150)


    #title for window

    root.title("Do as u want")
    root.mainloop()
except:
    messagebox.showerror("Opps","Error Occured")