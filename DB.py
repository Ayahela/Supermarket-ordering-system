import sqlite3
from tkinter import messagebox
import tkinter as tk
conn = sqlite3.connect("supermarket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Phone TEXT,
    bill_no TEXT          
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL UNIQUE
)
""")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT NOT NULL,
    CategoryID INTEGER,
    UnitPrice REAL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
)
""")
# إنشاء جدول الفواتير
cursor.execute("""
CREATE TABLE IF NOT EXISTS Bills (
    BillNumber INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS BillDetails (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    BillNumber INTEGER,
    ItemID INTEGER,
    Quantity INTEGER,
    Price REAL,
    FOREIGN KEY (BillNumber) REFERENCES Bills(BillNumber),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
)
""")

def insert_customer(name, phone, bill_number):
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (name, phone, bill_number) VALUES (?, ?, ?)", (name, phone, bill_number))
    conn.commit()
    conn.close()



def create_bill(customer_id, bill_number):
    cursor.execute("INSERT INTO Bills (BillNumber, CustomerID) VALUES (?, ?)", (bill_number, customer_id))
    conn.commit()

    
def clear_all_db(self):
    # 1. مسح قاعدة البيانات
    cursor.execute("DELETE FROM Customers")
    cursor.execute("DELETE FROM Bills")
    conn.commit()

    # 2. مسح واجهة المستخدم
    self.name_var.set("")
    self.phone_var.set("")
    self.bill_var.set("")

    for var in self.legumes_vars + self.household_vars + self.electrical_vars:
        var.set("0")

    self.textarea.delete("1.0", tk.END)

    messagebox.showinfo("تم", "تم مسح كل البيانات بنجاح")
conn.commit()
conn.close()
# --------------------------------------------------------



def add_bill(self):
    name = self.name_var.get().strip()
    phone = self.phone_var.get().strip()
    bill_no = self.bill_var.get().strip()

    if not name or not phone or not bill_no:
        messagebox.showerror("خطأ", "يرجى ملء كل الحقول")
        return

    try:
        bill_no = int(bill_no)
    except ValueError:
        messagebox.showerror("خطأ", "رقم الفاتورة لازم يكون رقم")
        return

    conn = sqlite3.connect("supermarket.db")
    cursor = conn.cursor()

    #customer_id = get_or_create_customer(name, phone)

    # محاولة إنشاء الفاتورة
    # try:
    #     create_bill(customer_id, bill_no)
    # except sqlite3.IntegrityError:
    #     messagebox.showerror("خطأ", f"رقم الفاتورة {bill_no} موجود بالفعل!")
    #     return

    # إضافة تفاصيل الفاتورة
    items = self.legumes_vars + self.household_vars + self.electrical_vars
    item_ids = list(range(1, len(items)+1))  # لازم يكون ترتيب الأصناف بنفس ترتيب الجدول

    for var, item_id in zip(items, item_ids):
        quantity = int(var.get())
        if quantity > 0:
            # هات السعر من جدول Items
            cursor.execute("SELECT UnitPrice FROM Items WHERE ItemID=?", (item_id,))
            result = cursor.fetchone()
            if result:
                price = result[0] * quantity
                cursor.execute("""
                    INSERT INTO BillDetails (BillNumber, ItemID, Quantity, Price)
                    VALUES (?, ?, ?, ?)
                """, (bill_no, item_id, quantity, price))

    conn.commit()
    conn.close()
    messagebox.showinfo("تم", f"تمت إضافة الفاتورة رقم {bill_no} بنجاح")

def charge_db(name_var, phone_var, bill_var,
              legumes_vars, legumes_names,
              household_vars, household_names,
              electrical_vars, electrical_names):
    
    import sqlite3
    from tkinter import messagebox

    conn = sqlite3.connect("supermarket.db")
    cursor = conn.cursor()

    name = name_var.get()
    phone = phone_var.get()
    bill_number = bill_var.get()

    if not name or not phone or not bill_number:
        messagebox.showwarning("تحذير", "يرجى إدخال اسم العميل ورقم الهاتف ورقم الفاتورة")
        return

    # التحقق إذا كان العميل موجود مسبقًا
    cursor.execute("SELECT CustomerID FROM Customers WHERE CustomerName=? AND Phone=?", (name, phone))
    result = cursor.fetchone()
    if result:
        customer_id = result[0]
    else:
        # إدخال عميل جديد
        cursor.execute("INSERT INTO Customers (CustomerName, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        customer_id = cursor.lastrowid

    # محاولة إدخال الفاتورة
    try:
        cursor.execute("INSERT INTO Bills (BillNumber, CustomerID) VALUES (?, ?)", (bill_number, customer_id))
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("خطأ", f"رقم الفاتورة {bill_number} موجود بالفعل!")
        return





    # إدخال الأصناف في تفاصيل الفاتورة
    def insert_items(category_vars, category_names):
        for var, name in zip(category_vars, category_names):
            qty = int(var.get())
            if qty > 0:
                cursor.execute("SELECT ItemID, UnitPrice FROM Items WHERE ItemName = ?", (name,))
                item = cursor.fetchone()
                if item:
                    item_id, unit_price = item
                    total = qty * unit_price
                    cursor.execute("""
                        INSERT INTO BillDetails (BillNumber, ItemID, Quantity, Price)
                        VALUES (?, ?, ?, ?)
                    """, (bill_number, item_id, qty, total))

    insert_items(legumes_vars, legumes_names)
    insert_items(household_vars, household_names)
    insert_items(electrical_vars, electrical_names)

    conn.commit()
    conn.close()

    messagebox.showinfo("تم", f"تم حفظ الفاتورة رقم {bill_number} بنجاح")