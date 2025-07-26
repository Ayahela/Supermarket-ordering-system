import sqlite3

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

conn.commit()
conn.close()

