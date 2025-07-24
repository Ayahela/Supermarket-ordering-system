from tkinter import*
import math , os ,random
from tkinter import messagebox
class super :
    def __init__(self,root):
        self.root=root
        self.root.geometry('1840x960')
        self.root.title('Super-Market')
        # self.root.resizable(False,False)
        self.root.iconbitmap(r'c:\superLogo.ico')
        title=Label(self.root,text='project management:super market',fg='white',bg='#0B2F3A',font=('tajawal',15))
        title.pack(fill=X)
        #========بيانات المستخدم========
        F1=Frame(self.root,bd=2,width=338,height=170,bg='#0B4C5F')
        F1.place(x=1189,y=35)
        tit=Label(F1,text='Customer data :',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='tomato')
        tit.place(x=0,y=0)
        his_name=Label(F1,text='Customer name',font=('tajawal',13),bg='#0B4C5F',fg='white')
        his_name.place(x=10,y=40)
        his_phone=Label(F1,text='Customer phone',font=('tajawal',13),bg='#0B4C5F',fg='white')
        his_phone.place(x=10,y=70)
        bill_num=Label(F1,text='Bill number',font=('tajawal',13),bg='#0B4C5F',fg='white')
        bill_num.place(x=10,y=100)

        Ent_name=Entry(F1,width=10)
        Ent_name.place(x=139,y=42)
        Ent_phone=Entry(F1,width=10)
        Ent_phone.place(x=139,y=72)
        Ent_num=Entry(F1,width=10)
        Ent_num.place(x=139,y=102)
        btn_customer=Button(F1,text='search',font=('tajawal',12),width=9,height=3,bg='white',)
        btn_customer.place(x=250,y=45)
        #======فاتورة=======
        tited=Label(F1,text='[Bills]',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        tited.place(x=135,y=135)
        F3=Frame(root,bd=2,width=338,height=450,bg='white')
        F3.place(x=1189,y=205)
        SCROLL_y=Scrollbar(F3,orient='vertical',)
        self.textarea=Text(F3,yscrollcommand=SCROLL_y.set,width=26,height=25)
        SCROLL_y.pack(side=RIGHT,fill=Y)
        SCROLL_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
root=Tk()
ob=super(root)
root.mainloop()