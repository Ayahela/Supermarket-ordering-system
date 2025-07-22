from tkinter import *
from tkinter import messagebox
import webbrowser    #فتح المتصفح
import os  # التفاعل مع نظام التشغيل
import sys  # التعامل مع النظام 
pro=Tk()
pro.geometry('800x450+280+50')    #from left 280 #from  top 50
pro.resizable(False,False)
pro.title('Supermarket')
pro.iconbitmap(r'C:\super.ico')
title=Label(pro,text='Super Market System',fg='gold',bg='black',font=('tajwal',16,'bold'))
title.pack(fill='x')  #عشان اخلي السطر كله ب اسود
pro.mainloop()