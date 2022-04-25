from tkinter import *
import pandas as pd
from tkinter import messagebox
import phonenumbers



f= ('Times',14)
f1 = ('Times',12)

def submit():
   
    
    
    
    
    # checking reqirements
    E1=phone_entry.get()
    E2 = complaint_entry.get()
   
    if E1 == "":
        messagebox.showwarning("man","Phone number must man")
    if E2 == "":
        messagebox.showwarning("man","complaint must man")
   
    else:
        E1 = phonenumbers.parse("+91"+E1)
        f1=(phonenumbers.is_valid_number(E1))
        if f1==True:
            messagebox.showinfo("sorry for inconviniance","Hope it will never reflect again")
            path = 'Data\Complaints.xlsx'
            K = pd.read_excel(path)
        
            #Adding elements from entery box
            seriesA = K['Phone_Number']
            seriesB = K['Complaint']
        
            
            A = pd.Series(phone_entry.get())
            B = pd.Series(complaint_entry.get())
            
            
            seriesA = seriesA.append(A)
            seriesB = seriesB.append(B)
            
            
            L = pd.DataFrame({"Phone_Number":seriesA,"Complaint":seriesB})
            L.to_excel(path,index=False)
            # deleating after submit
            phone_entry.delete(0,END)
            complaint_entry.delete(0,END)
        else:
            messagebox.showwarning("man",'enter valid number')
    
    
   




root = Tk()

root.geometry('500x500')

#for phone number

Phone_Number=Label(root,text="Enter Phone Number",font=f1).grid(row=1,column=2)

PhoneNumber_Value= IntVar

phone_entry = Entry(root,textvariable=PhoneNumber_Value,font=f,bg='#CCCCCC')
phone_entry.grid(row=1 ,column=3)

#for complaint

complain=Label(root,text="Enter Complaint",font= f1).grid(row=2,column=2)

complaint_Value= StringVar

complaint_entry = Entry(root,textvariable=complaint_Value,font=f,bg='#CCCCCC')
complaint_entry.grid(row=2 ,column=3,
       #     padx=10,
       #     pady=10,
      #      ipadx=10,      ipady=30
      )



btn = Button(root,text="Submit Complaint",command=submit,font=('roboto',12)).grid(row=3,column=3)

btn2 = Button(root,text="         Back         ",command=quit,font = ('roboto',12)).grid(row=4,column=3)


root.mainloop()
