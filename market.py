from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import os  
import sys
from super import super  
pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(False, False)
pro.title('Supermarket')
pro.iconbitmap(r'C:\super.ico')

# العنوان
title = Label(pro, text='Super Market System', fg='#F6B323', bg='black', font=('Arial', 20, 'bold'))
title.pack(fill='x')

#forth video(fun of each button)
u1='https://www.facebook.com/onlineshop00432'
u2='https://t.me/digitalearningwithprishangwithprisha'
u3='https://www.youtube.com/shorts/8KSMwP2fbGg'
def Open1():
    webbrowser.open_new(u1)
def OPen2():
    webbrowser.open_new(u2)
def OPen3():
    webbrowser.open_new(u3)    
def about1():
    messagebox.showinfo('تيم خليها على الله','develepoer')
def about2():
    messagebox.showinfo('project','supermarket project on tinkerkat with python:)')      

def log():
    user = En1.get()
    password = En2.get()
    if user == 'BFCAI' and password == 'supermarket':
        pro.destroy()
        root = tk.Tk()
        app = super(root)
        root.mainloop()
    else:
        messagebox.showerror('error', 'sorry password is wrong')
   

# المستطيل الأحمر
F1 = Frame(pro, width=230, height=500, bg='#0B2F3A')
F1.pack(side='right', fill='y')  # ممكن كمان تستخدم fill='both' لو عايزة يغطي كامل الطول
Title1=Label(F1,text='Supermarket Project',bg='#0B2F3A' ,fg='white',font=('Arial',12, 'bold')) 
Title1.place(x=25,y=10)
Title2=Label(F1,text='Developed by:Team',bg='#0B2F3A',fg='white',font=('Arial',12, 'bold'))
Title2.place(x=25,y=50)
Title3=Label(F1,text='Contact With Us',bg='#0B2F3A' ,fg='white',font=('Arial',12, 'bold'))
Title3.place(x=25,y=90)
B1=Button(F1,text='Account On Facebook',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'),command=Open1)
B1.place(x=1,y=130)
B2=Button(F1,text='Account On Telegram',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'),command=OPen2)
B2.place(x=1,y=180)
B3=Button(F1,text='channel On Youtube',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'),command=OPen3)
B3.place(x=1,y=230)
B4=Button(F1,text='Overview Of Our Project',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'),command=about1)
B4.place(x=1,y=280)
B5=Button(F1,text='Communication With Us',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'))
B5.place(x=1,y=330)
B6=Button(F1,text='Close The Website',width=26,fg='black',bg='#F6B323',font=('Arial',11, 'bold'),command=quit)
B6.place(x=1,y=380)

# تحميل وتغيير حجم الصورة
# الصورة الأولى
image = Image.open(r'C:\shop.png')
image = image.resize((365,365))  # ضبط الحجم ليتوافق مع place
photo = ImageTk.PhotoImage(image)
image_label = Label(pro, image=photo, bd=0)  # إزالة الإطار الأسود
image_label.image = photo  # مهم جدًا علشان الصورة ما تختفيش
image_label.place(x=85, y=40, width=450, height=300)

# الجزء اللي تحت
F2 = Frame(pro, width=570, height=170, bg='#0B2F3A')
F2.place(x=0, y=330)

# صورة تسجيل الدخول
image2 = Image.open(r'C:\login(1).png')
image2 = image2.resize((70, 70))
image2_tk = ImageTk.PhotoImage(image2)
image2_label = Label(pro, image=image2_tk, bg="#F6B323")
image2_label.image = image2_tk
image2_label.place(x=430, y=335, width=120, height=110)

# # المدخلات
L1 = Label(F2, text='Username', fg='gold', bg='#0B2F3A', font=('tajawal', 15))
L1.place(x=330, y=22)

L2 = Label(F2, text='Password', fg='gold', bg='#0B2F3A', font=('tajawal', 15))
L2.place(x=330, y=66)

En1 = Entry(F2, font=('tajawal', 12), justify='center')
En1.place(x=130, y=26)

En2 = Entry(F2, font=('tajawal', 12), justify='center', show='*')  # تخفي كلمة السر
En2.place(x=130, y=71)

B = Button(F2, text='login', bg='#F6B323', font=('bold', 17), command=log)
# B.place(x=4, y=71)
B.place(x=10, y=25, width=110, height=70 )

pro.mainloop()
