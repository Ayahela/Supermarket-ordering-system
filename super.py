from tkinter import *
import random
from tkinter import messagebox
from DB import create_bill,insert_customer 

class super :
     def add_bill(self):
      bill_no = self.Ent_num.get()
      total_price=self.total_all
      quantity=self.quantity
      category_price1=self.total_legumes
      category_price2= self.total_household
      category_price3= self.total_electrical
      # Insert bill data into the database
      create_bill(bill_no, quantity,category_price1,category_price2,category_price3,total_price)
      self.charge_total()
     def add_customer(self):
      CustomerName = self.Ent_name.get()
      phone = self.Ent_phone.get()
      bill_no = self.Ent_num.get()

      # Insert customer data into the database
      insert_customer(CustomerName, phone, bill_no)

      # Display customer data in the bill area
      self.welcome()

     def exit_app(self):
       confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
       if confirm:
         self.root.destroy()

           
     def charge_total(self):

        
        

        # البقوليات
        legumes_vars = [
         self.q1, self.q2, self.q3, self.q4, self.q5, self.q6, self.q7, self.q8, self.q9,
         self.q10, self.q11, self.q12, self.q13, self.q14, self.q15, self.q16, self.q17, self.q18
    ]
        legumes_names = [
        'rice', 'bulgur', 'beans', 'lentils', 'noodles', 'freca', 'homos', 'fool', 'salt',
        'sugar', 'papper', 'red papper', 'green beans', 'lupinus', 'wheat', 'barley', 'oats', 'atom'
    ]
        for i in range(18):
          try:
            qty1 = int(legumes_vars[i].get())
          except:
            qty1 = 0
          if qty1 > 0:
            price = qty1 * self.legumes_prices[i]
            self.total_legumes += price
            self.textarea.insert(END, f"\n{price}\t{qty1}\t{legumes_names[i]}")

    # أدوات منزلية
        household_vars = [
        self.qq1, self.qq2, self.qq3, self.qq4, self.qq5, self.qq6, self.qq7, self.qq8,
        self.qq9, self.qq10, self.qq11, self.qq12, self.qq13, self.qq14, self.qq15, self.qq16,
        self.qq17, self.qq18
    ]
        household_names = [
        'strainer', 'plate', 'glass', 'teapot', 'knife', 'fork', 'pot', 'basket', 'spoons',
        'tray', 'mixing bowl', 'can opener', 'peeler', 'cutting board', 'corer', 'trash bin', 'duster', 'bags'
    ]
        for i in range(18):
           try:
            qty2 = int(household_vars[i].get())
           except:
            qty2 = 0
           if qty2 > 0:
            price = qty2 * self.household_prices[i]
            self.total_household+= price
            self.textarea.insert(END, f"\n{price}\t{qty2}\t{household_names[i]}")

    # الأجهزة الكهربائية
        electrical_vars = [
        self.qqq1, self.qqq2, self.qqq3, self.qqq4, self.qqq5, self.qqq6, self.qqq7,
        self.qqq8, self.qqq9, self.qqq10, self.qqq11, self.qqq12, self.qqq13, self.qqq14
    ]
        electrical_names = [
        'vacuum cleaner', 'television', 'washing machine', 'microwave', 'blender', 'gas oven',
        'electric fryer', 'ceiling fan', 'standing fan', 'television 32', 'television 43',
        'water filter', 'iron', 'cooler'
    ]
        for i in range(14):
           try:
            qty3 = int(electrical_vars[i].get())
           except:
            qty3 = 0
           if qty3 > 0:
            price = qty3 * self.electrical_prices[i]
            self.total_electrical += price
            self.textarea.insert(END, f"\n{price}\t{qty3}\t{electrical_names[i]}")

    # اجمالي الاقسام
        self.legumes.set(str(self.total_legumes))
        self.householdsupplies.set(str(self.total_household))
        self.electricalappliances.set(str(self.total_electrical))

        self.textarea.insert(END, "\n" + "=" * 48)
        self.total_all = self.total_legumes + self.total_household + self.total_electrical
        self.textarea.insert(END, f"\nTotal Bill: {self.total_all}")
        self.textarea.insert(END, "\n" + "=" * 48)
        self.quantity=qty1+qty2+qty3
        

         

     def __init__(self,root):
        self.total_all = 0
        self.total_legumes = 0
        self.total_household = 0
        self.total_electrical = 0
        self.quantity = 0
            # === الأسعار لكل قسم ===
        self.legumes_prices = [
            15, 12, 18, 20, 10, 14, 16, 13, 5, 10,
            8, 9, 17, 11, 7, 6, 8, 21
        ]
        self.household_prices = [
            25, 10, 8, 30, 12, 8, 40, 20, 10, 15,
            35, 18, 14, 22, 16, 50, 10, 6
        ]
        self.electrical_prices = [
            800, 1200, 1400, 600, 350, 1500, 1000,
            700, 750, 1300, 1600, 950, 500, 2000
        ]

        self.root=root
        self.root.geometry('1840x960')
        self.root.title('Super-Market')
      #   self.root.resizable(False,False)
        self.root.iconbitmap(r'c:\superLogo.ico')
        title=Label(self.root,text='project management:super market',fg='white',bg='#0B2F3A',font=('tajawal',15))
        title.pack(fill=X)
        self.bill=StringVar()
        x=random.randint(1000,9999)
        self.bill.set(str(x))
        self.namo=StringVar()
        self.phono=StringVar()
        self.name_var = StringVar()
        self.phone_var = StringVar()
        self.bill_var = StringVar()
        ##############################
        def clear_all_entries():
          clear
          for entry in entries:
           entry.delete(0, END)
         ###############################
        #--------variables-------------
        self.legumes=StringVar()
        self. householdsupplies=StringVar()
        self.electricalappliances=StringVar()
        #==============================
        #=====[legumes from q1=>q18]===
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()
     #=====[House hold suppllies from qq1=>qq18]===
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
      
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()
     #=====[Electrical Appliances from qqq1=>qqq15]===
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()
        #===========================
        #buyer information variables
        #===========================
        self.namo=StringVar()
        self.phono=StringVar()
        self.bill=StringVar()
        x=random.randint(1000,9999)
        self.bill.set(str(x))
        #==========================
        #Total Cost Variables
        #==========================
        self.legumes=StringVar()
        self. householdsupplies=StringVar()
        self.electricalappliances=StringVar()

     
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


<<<<<<< HEAD
        Ent_name=Entry(F1,textvariable=self.namo,width=10)
        Ent_name.place(x=139,y=42)
        Ent_phone=Entry(F1,textvariable=self.phono,width=10)
        Ent_phone.place(x=139,y=72)
        Ent_num=Entry(F1,textvariable=self.bill,width=10)
        Ent_num.place(x=139,y=102)
        btn_customer=Button(F1,text='Add',font=('tajawal',12),width=8,height=2,bg='white',command=self.welcome)
        btn_customer.place(x=250,y=50)
=======
        self.Ent_name=Entry(F1,textvariable=self.namo,width=10)
        self.Ent_name.place(x=139,y=42)
        self.Ent_phone=Entry(F1,textvariable=self.phono,width=10)
        self.Ent_phone.place(x=139,y=72)
        self.Ent_num=Entry(F1,textvariable=self.bill,width=10)
        self.Ent_num.place(x=139,y=102)
        self.btn_customer=Button(F1,text='Add',font=('tajawal',12),width=9,height=3,bg='white',command=self.add_customer)
        self.btn_customer.place(x=250,y=45)
>>>>>>> 04432d8330286c52679df75c3794643c825df4af
        #======فاتورة=======
        tited=Label(F1,text='[Bills]',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        tited.place(x=135,y=135)
        F3=Frame(root,bd=2,width=338,height=450,bg='white')
        F3.place(x=1200,y=205)
        SCROLL_y=Scrollbar(F3,orient='vertical',)
        self.textarea=Text(F3,yscrollcommand=SCROLL_y.set,width=37,height=25)
        SCROLL_y.pack(side=RIGHT,fill=Y)
        SCROLL_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #------price-------
        F4=Frame(root,bd=2,width=720,height=122,bg='#0B4C5F')
        F4.place(x=790,y=650)
        hesab = Button(F4, text='charge', width=13, height=1, font='tajawal', bg='#DBA901', command=self.add_bill
        )
        hesab.place(x=560,y=10)
      #   fatora=Button(F4,text='import charge',width=13,height=1,font='tajawal',bg='#DBA901')
      #   fatora.place(x=560,y=55)
        clear=Button(F4,text='Clear all',width=13,height=1,font='tajawal',bg='#DBA901',command=clear_all_entries )
        clear.place(x=405,y=10)
        exite=Button(F4,text='exite',width=13,height=1,font='tajawal',bg='#DBA901',command=self.exit_app)
        exite.place(x=490,y=55)

        lblo1=Label(F4,text='total charge for legumes',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo1.place(x=10,y=10)

        lblo2=Label(F4,text='total charge for householdsupplies',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo2.place(x=10,y=40)
        
        lblo2=Label(F4,text='total charge for electricalappliances',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo2.place(x=10,y=70)

        ento1=Entry(F4,textvariable=self.legumes,width=24)
        ento1.place(x=250,y=12)
        ento2=Entry(F4,textvariable=self. householdsupplies,width=24)
        ento2.place(x=250,y=42)
        ento3=Entry(F4,textvariable=self.electricalappliances ,width=24)
        ento3.place(x=250,y=72)
        entries=[ento1,ento2,ento3]

        #-------items[1]---------
        FF1=Frame(root,bd=2,width=380,height=745,bg='#0B4C5F')
        FF1.place(x=1,y=35)
        t=Label(FF1,text='legumes',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        t.place(x=122,y=0)
        bq1=Label(FF1,text='rice',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq1.place(x=30,y=50)
        bq2=Label(FF1,text='bulgur',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq2.place(x=30,y=90)
        bq3=Label(FF1,text='beans',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq3.place(x=30,y=130)
        bq4=Label(FF1,text='lentils',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq4.place(x=30,y=170)
        bq5=Label(FF1,text='Noodles',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq5.place(x=30,y=210)
        bq6=Label(FF1,text='freca',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq6.place(x=30,y=250)
        bq7=Label(FF1,text='homos',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq7.place(x=30,y=290)
        bq8=Label(FF1,text='fool',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq8.place(x=30,y=330)
        bq9=Label(FF1,text='salt',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq9.place(x=30,y=370)
        bq10=Label(FF1,text='sugar',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq10.place(x=30,y=410)
        bq11=Label(FF1,text='papper',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq11.place(x=30,y=450)
        bq12=Label(FF1,text='red papper',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq12.place(x=30,y=490)
        bq13=Label(FF1,text='grean beans',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq13.place(x=30,y=530)
        bq14=Label(FF1,text='Lupinus',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq14.place(x=30,y=570)
        bq15=Label(FF1,text='wheat',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq15.place(x=30,y=610)
        bq16=Label(FF1,text='barley',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq16.place(x=30,y=650)
        bq17=Label(FF1,text='oats',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq17.place(x=30,y=680)
        bq18=Label(FF1,text='atom',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bq18.place(x=30,y=710)

        bqent1=Entry(FF1,textvariable=self.q1,width=12)
        bqent1.place(x=170,y=55)

        bqent2=Entry(FF1,textvariable=self.q2,width=12)
        bqent2.place(x=170,y=95)
        bqent3=Entry(FF1,textvariable=self.q3,width=12)
        bqent3.place(x=170,y=135)
        bqent4=Entry(FF1,textvariable=self.q4,width=12)
        bqent4.place(x=170,y=175)
        bqent5=Entry(FF1,textvariable=self.q5,width=12)
        bqent5.place(x=170,y=215)
        bqent6=Entry(FF1,textvariable=self.q6,width=12)
        bqent6.place(x=170,y=255)
        bqent7=Entry(FF1,textvariable=self.q7,width=12)
        bqent7.place(x=170,y=295)
        bqent8=Entry(FF1,textvariable=self.q8,width=12)
        bqent8.place(x=170,y=335)
        bqent9=Entry(FF1,textvariable=self.q9,width=12)
        bqent9.place(x=170,y=375)
        bqent10=Entry(FF1,textvariable=self.q10,width=12)
        bqent10.place(x=170,y=415)
        bqent11=Entry(FF1,textvariable=self.q11,width=12)
        bqent11.place(x=170,y=455)
        bqent12=Entry(FF1,textvariable=self.q12,width=12)
        bqent12.place(x=170,y=495)
        bqent13=Entry(FF1,textvariable=self.q13,width=12)
        bqent13.place(x=170,y=535)
        bqent14=Entry(FF1,textvariable=self.q14,width=12)
        bqent14.place(x=170,y=575)
        bqent15=Entry(FF1,textvariable=self.q15,width=12)
        bqent15.place(x=170,y=615)
        bqent16=Entry(FF1,textvariable=self.q16,width=12)
        bqent16.place(x=170,y=655)
        bqent17=Entry(FF1,textvariable=self.q17,width=12)
        bqent17.place(x=170,y=685)
        bqent18=Entry(FF1,textvariable=self.q18,width=12)
        bqent18.place(x=170,y=715)
#------------items2-----------#
        FF2=Frame(root,bd=2,width=380,height=745,bg='#0B4C5F')
        FF2.place(x=395,y=35)
        tt=Label(FF2,text='Household supplies',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        tt.place(x=122,y=0)
        bqr1=Label(FF2,text='strainer',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr1.place(x=30,y=50)
        bqr2=Label(FF2,text='plate',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr2.place(x=30,y=90)
        bqr3=Label(FF2,text='glass',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr3.place(x=30,y=130)
        bqr4=Label(FF2,text='teapot',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr4.place(x=30,y=170)
        bqr5=Label(FF2,text='knife',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr5.place(x=30,y=210)
        bqr6=Label(FF2,text='fork',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr6.place(x=30,y=250)
        bqr7=Label(FF2,text='pot',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr7.place(x=30,y=290)
        bqr8=Label(FF2,text='basket',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr8.place(x=30,y=330)
        bqr9=Label(FF2,text='spoons',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr9.place(x=30,y=370)
        bqr10=Label(FF2,text='tray',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr10.place(x=30,y=410)
        bqr11=Label(FF2,text='maxing bowl',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr11.place(x=30,y=450)
        bqr12=Label(FF2,text='can opener',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr12.place(x=30,y=490)
        bqr13=Label(FF2,text='peeler',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr13.place(x=30,y=530)
        bqr14=Label(FF2,text='cutting board',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr14.place(x=30,y=570)
        bqr15=Label(FF2,text='corer',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr15.place(x=30,y=610)
        bqr16=Label(FF2,text='trash bin',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr16.place(x=30,y=650)
        bqr17=Label(FF2,text='duster',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr17.place(x=30,y=680)
        bqr18=Label(FF2,text='bags',font=('tajawal',14),bg='#0B4C5F',fg='white')
        bqr18.place(x=30,y=710)

        bqent1=Entry(FF2,textvariable=self.qq1,width=12)
        bqent1.place(x=170,y=55)

        bqrnt2=Entry(FF2,textvariable=self.qq2,width=12)
        bqrnt2.place(x=170,y=95)
        bqrnt3=Entry(FF2,textvariable=self.qq3,width=12)
        bqrnt3.place(x=170,y=135)
        bqrnt4=Entry(FF2,textvariable=self.qq4,width=12)
        bqrnt4.place(x=170,y=175)
        bqrnt5=Entry(FF2,textvariable=self.qq5,width=12)
        bqrnt5.place(x=170,y=215)
        bqrnt6=Entry(FF2,textvariable=self.qq6,width=12)
        bqrnt6.place(x=170,y=255)
        bqrnt7=Entry(FF2,textvariable=self.qq7,width=12)
        bqrnt7.place(x=170,y=295)
        bqrnt8=Entry(FF2,textvariable=self.qq8,width=12)
        bqrnt8.place(x=170,y=335)
        bqrnt9=Entry(FF2,textvariable=self.qq9,width=12)
        bqrnt9.place(x=170,y=375)
        bqrnt10=Entry(FF2,textvariable=self.qq10,width=12)
        bqrnt10.place(x=170,y=415)
        bqrnt11=Entry(FF2,textvariable=self.qq11,width=12)
        bqrnt11.place(x=170,y=455)
        bqrnt12=Entry(FF2,textvariable=self.qq12,width=12)
        bqrnt12.place(x=170,y=495)
        bqrnt13=Entry(FF2,textvariable=self.qq13,width=12)
        bqrnt13.place(x=170,y=535)
        bqrnt14=Entry(FF2,textvariable=self.qq14,width=12)
        bqrnt14.place(x=170,y=575)
        bqrnt15=Entry(FF2,textvariable=self.qq15,width=12)
        bqrnt15.place(x=170,y=615)
        bqrnt16=Entry(FF2,textvariable=self.qq16,width=12)
        bqrnt16.place(x=170,y=655)
        bqrnt17=Entry(FF2,textvariable=self.qq17,width=12)
        bqrnt17.place(x=170,y=685)
        bqrnt18=Entry(FF2,textvariable=self.qq18,width=12)
        bqrnt18.place(x=170,y=715)

        #------------items3-----------#
        FF3=Frame(root,bd=2,width=380,height=610,bg='#0B4C5F')
        FF3.place(x=790,y=35)
       
        
        ttt=Label(FF3,text='Electrical appliances',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
        ttt.place(x=122,y=0)
        br1=Label(FF3,text='vacuum cleaner',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br1.place(x=30,y=50)
        br2=Label(FF3,text='television',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br2.place(x=30,y=90)
        br3=Label(FF3,text='washing machine ',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br3.place(x=30,y=130)
        br4=Label(FF3,text='microwave',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br4.place(x=30,y=170)
        br5=Label(FF3,text='blender',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br5.place(x=30,y=210)
        br6=Label(FF3,text='gas oven',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br6.place(x=30,y=250)
        br7=Label(FF3,text='electric fryer',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br7.place(x=30,y=290)
        br8=Label(FF3,text='celling fan',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br8.place(x=30,y=330)
        br9=Label(FF3,text='standing fan',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br9.place(x=30,y=370)
        br10=Label(FF3,text='television 32',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br10.place(x=30,y=410)
        br11=Label(FF3,text='television 43',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br11.place(x=30,y=450)
        br12=Label(FF3,text=' water filter',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br12.place(x=30,y=490)
        br13=Label(FF3,text=' iron',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br13.place(x=30,y=530)
        br14=Label(FF3,text='cooler',font=('tajawal',14),bg='#0B4C5F',fg='white')
        br14.place(x=30,y=570)
      
       

        bqent1=Entry(FF3,textvariable=self.qqq1,width=12)
        bqent1.place(x=190,y=55)

        bqrnt2=Entry(FF3,textvariable=self.qqq2,width=12)
        bqrnt2.place(x=190,y=95)
        bqrnt3=Entry(FF3,textvariable=self.qqq3,width=12)
        bqrnt3.place(x=190,y=135)
        bqrnt4=Entry(FF3,textvariable=self.qqq4,width=12)
        bqrnt4.place(x=190,y=175)
        bqrnt5=Entry(FF3,textvariable=self.qqq5,width=12)
        bqrnt5.place(x=190,y=215)
        bqrnt6=Entry(FF3,textvariable=self.qqq6,width=12)
        bqrnt6.place(x=190,y=255)
        bqrnt7=Entry(FF3,textvariable=self.qqq7,width=12)
        bqrnt7.place(x=190,y=295)
        bqrnt8=Entry(FF3,textvariable=self.qqq8,width=12)
        bqrnt8.place(x=190,y=335)
        bqrnt9=Entry(FF3,textvariable=self.qqq9,width=12)
        bqrnt9.place(x=190,y=375)
        bqrnt10=Entry(FF3,textvariable=self.qqq10,width=12)
        bqrnt10.place(x=190,y=415)
        bqrnt11=Entry(FF3,textvariable=self.qqq11,width=12)
        bqrnt11.place(x=190,y=455)
        bqrnt12=Entry(FF3,textvariable=self.qqq12,width=12)
        bqrnt12.place(x=190,y=495)
        bqrnt13=Entry(FF3,textvariable=self.qqq13,width=12)
        bqrnt13.place(x=190,y=535)
        bqrnt14=Entry(FF3,textvariable=self.qqq14,width=12)
        bqrnt14.place(x=190,y=575)
        self.welcome()
        #products prices#
        # PRICE_LEGUMES = 10
        # PRICE_HOUSEHOLD = 15
        # PRICE_ELCTRICAL = 25

     def welcome(self):
         self.textarea.delete('1.0',END)
         self.textarea.insert(END,"\t welcome to super market ")
         self.textarea.insert(END,"\n================================================")
         self.textarea.insert(END,f"\n\t B.NUM : {self.bill.get()}")
         self.textarea.insert(END,f"\n\t  NAME : {self.namo.get()}  ")
         self.textarea.insert(END,f"\n\t PHONE : {self.phono.get()} ")
         self.textarea.insert(END,f"\n\t")
         self.textarea.insert(END,"\n================================================")
         self.textarea.insert(END,f"\n price \t  number \t  product  ")
         self.textarea.insert(END,"\n================================================")
     
# root=Tk()
# ob=super(root)
# root.mainloop()