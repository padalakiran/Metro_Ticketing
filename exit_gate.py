import cv2
import numpy as np
from pyzbar.pyzbar import decode
import mysql.connector



mydb = mysql.connector.connect(
      host="localhost",
        user="root",
        password=" my sql password",
        database="dtabase name"
)


mycursor = mydb.cursor()

wCam, hCam =640,480

#img=cv2.imread('1.jpg')
#code=decode(img)

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)


    
i=1
while i==1:
    success,img = cap.read()
    for barcode in decode(img):
        #print(barcode.data)
        myData= barcode.data.decode('utf-8')
        #print(myData)
        sql="select * from tickets;"
        
        mycursor.execute(sql)
        a = mycursor.fetchall()
       # print(a)
        for i in range(len(a)):
           if a[i][0]==myData and a[i][1]==1:
               
                if a[i][1]==1:
                    mydb.commit()
                    myOutput='Enter Corre'
                    myColor =(0,0,255)
                    TextColor = (0,0,255)
               
                sql = """DELETE FROM tickets WHERE code=%s;"""
                valus=[(myData)]
                mycursor.execute(sql,valus) 
                mydb.commit()
                myOutput='Aurthorized'
                myColor =(0,255,0)
                TextColor = (0,255,0)
                i+=1
               
               
               
               
               
               
               
               
               
               
               

           else:
                myOutput='Un-Aurthorized'
                myColor =(0,0,255)
                TextColor = (0,0,255)
                i=1



        pts = np.array([barcode.polygon],np.int32)
        pts =pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1],), cv2.FONT_HERSHEY_TRIPLEX,0.9,TextColor),2        
        

        #print(code)
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('result',img)
    cv2.waitKey(1)
