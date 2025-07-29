import sqlite3
from tkinter import messagebox
import tkinter as tk
conn = sqlite3.connect("supermarket.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS Customers")

# Create the table again with correct structure
cursor.execute("""
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerName TEXT NOT NULL,
    Phone TEXT,
    bill_no TEXT
)
""")
conn.commit()

#catogories
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL UNIQUE
)
""")


#Items
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT NOT NULL,
    CategoryID INTEGER,
    UnitPrice REAL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
)
""")
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS BILLSS (
     bill_no INTEGER,
     quantity INTEGER,
     category1_price FLOAT,
     category2_price  FLOAT,
     category3_price FLOAT,                    
     total_price FLOAT                 
                        
)
""")
# #BILLS details table

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS BillDetails (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     BillNumber INTEGER,
#     ItemID INTEGER,
#     Quantity INTEGER,
#     Price REAL,
#     FOREIGN KEY (BillNumber) REFERENCES Bills(BillNumber),
#     FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
# )
# """)

def insert_customer(name, phone, bill_number):
    conn = sqlite3.connect('supermarket.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Customers (CustomerName, phone, bill_no) VALUES (?, ?, ?)", (name, phone, bill_number))
    conn.commit()
   

def create_bill(bill_no, quantity,category1_price,category2_price,category3_price,total_price):
    conn = sqlite3.connect('supermarket.db')
    cursor.execute("INSERT INTO BILLSS (bill_no, quantity,category1_price,category2_price,category3_price,total_price) VALUES (?, ?, ?, ?, ?, ?)", (bill_no, quantity,category1_price,category2_price,category3_price,total_price))
    conn.commit()

# --------------------------------------------------------

def insert_categories():
    categories = ["Legumes", "Household supplies", "Electrical appliances"]
    for category in categories:
        cursor.execute("INSERT INTO Categories(CategoryName) VALUES (?)", (category,))
    conn.commit()
    conn.close()