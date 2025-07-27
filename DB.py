import sqlite3
from tkinter import messagebox
import tkinter as tk
conn = sqlite3.connect("supermarket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Phone TEXT
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

# دالة لإحضار أو إدخال العميل
def get_or_create_customer(name, phone):
    cursor.execute("SELECT CustomerID FROM Customers WHERE CustomerName=? AND Phone=?", (name, phone))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute("INSERT INTO Customers (CustomerName, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        return cursor.lastrowid


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
def charge_db():
    import sqlite3
    from tkinter import messagebox

    conn = sqlite3.connect("supermarket.db")
    cursor = conn.cursor()

    # قراءة بيانات العميل والفاتورة من الواجهة
    name = name_var.get()
    phone = phone_var.get()
    bill_number = bill_var.get()

    if not name or not phone or not bill_number:
        messagebox.showwarning("تحذير", "يرجى إدخال اسم العميل ورقم الهاتف ورقم الفاتورة")
        return

    # الحصول على ID العميل أو إضافته
    cursor.execute("SELECT CustomerID FROM Customers WHERE CustomerName=? AND Phone=?", (name, phone))
    result = cursor.fetchone()
    if result:
        customer_id = result[0]
    else:
        cursor.execute("INSERT INTO Customers (CustomerName, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        customer_id = cursor.lastrowid

    # إدخال الفاتورة
    try:
        cursor.execute("INSERT INTO Bills (BillNumber, CustomerID) VALUES (?, ?)", (bill_number, customer_id))
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("خطأ", f"رقم الفاتورة {bill_number} موجود بالفعل!")
        return

    # حفظ الأصناف
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

conn.commit()
conn.close()