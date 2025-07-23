from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import os  
import sys
pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(False, False)
pro.title('Supermarket')
pro.iconbitmap(r'C:\super.ico')
# العنوان
title = Label(pro, text='Super Market System', fg='yellow', bg='black', font=('Arial', 20, 'bold'))
title.pack(fill='x')

# المستطيل الأحمر
F1 = Frame(pro, width=230, height=500, bg='#0B2F3A')
F1.pack(side='right', fill='y')  # ممكن كمان تستخدم fill='both' لو عايزة يغطي كامل الطول
Title1=Label(F1,text='Supermarket Project',bg='#0B2F3A' ,fg='white',font=('Arial',12, 'bold')) 
Title1.place(x=25,y=10)
Title2=Label(F1,text='Developed by:Team',bg='#0B2F3A',fg='white',font=('Arial',12, 'bold'))
Title2.place(x=25,y=50)
Title3=Label(F1,text='Contact With Us',bg='#0B2F3A' ,fg='white',font=('Arial',12, 'bold'))
Title3.place(x=25,y=90)
B1=Button(F1,text='Account On Facebook',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B1.place(x=1,y=130)
B2=Button(F1,text='Account On Telegram',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B2.place(x=1,y=180)
B3=Button(F1,text='channel On Youtube',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B3.place(x=1,y=230)
B4=Button(F1,text='Overview Of Our Project',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B4.place(x=1,y=280)
B5=Button(F1,text='Communication With Us',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B5.place(x=1,y=330)
B6=Button(F1,text='Close The Website',width=26,fg='black',bg='#DBA901',font=('Arial',11, 'bold'))
B6.place(x=1,y=380) 
# تحميل وتغيير حجم الصورة
image = Image.open(r'C:\shop.JPG')
image = image.resize((250, 250))  # حجم مناسب للواجهة
photo = ImageTk.PhotoImage(image)

# وضع الصورة في منتصف المساحة الرمادية
label = Label(pro, image=photo, bg='#F2F2F2')  # خلي الخلفية زي الخلفية الرمادية
label.image = photo
label.place(x=275, y=100)  # تقريبًا في النص (800 عرض - 250 للصورة - 230 للفريم = 320 فراغ)

pro.mainloop()
