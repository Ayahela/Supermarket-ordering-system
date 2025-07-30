import sqlite3 

# الاتصال وإنشاء الجداول
con = sqlite3.connect('supermarket.db')
cursor = con.cursor()

# جدول العملاء
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customerId INTEGER PRIMARY KEY AUTOINCREMENT,
        customerName TEXT NOT NULL,
        phone TEXT,
        bill_no TEXT
    )
""")

# جدول الفئات
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL
    )
""")

# جدول المنتجات
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Items (
        ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
        ItemName TEXT NOT NULL,
        CategoryID INTEGER,
        UnitPrice REAL,
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
""")

# جدول الفواتير
cursor.execute("""
    CREATE TABLE IF NOT EXISTS BILLSS (
        bill_no INTEGER,
        category1_price FLOAT,
        category2_price FLOAT,
        category3_price FLOAT,
        total_price FLOAT
    )
""")

con.commit()
con.close()

# --------------------------------------
# دوال التعامل مع الداتا

def showAllCustomers():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customers')
    data = cursor.fetchall()
    conn.close()
    return data

def insert_customer(name, phone, bill_number):
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (CustomerName, phone, bill_no) VALUES (?, ?, ?)",
                   (name, phone, bill_number))
    conn.commit()
    conn.close()

def create_bill(bill_no, category1_price, category2_price, category3_price, total_price):
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO BILLSS (bill_no, category1_price, category2_price, category3_price, total_price)
        VALUES (?, ?, ?, ?, ?)
    """, (bill_no, category1_price, category2_price, category3_price, total_price))

    conn.commit()
    conn.close()

def insert_categories():
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    categories = ["Legumes", "Household supplies", "Electrical appliances"]
    for category in categories:
        try:
            cursor.execute("INSERT INTO Categories(category_name) VALUES (?)", (category,))
        except sqlite3.IntegrityError:
            pass 
    conn.commit()
    conn.close()
