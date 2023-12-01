# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
import os
from sqlalchemy import create_engine, text

# DEFINE THE DATABASE CREDENTIALS
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
db_connection_string,
connect_args={
  "ssl": {
    "ssl_ca": ""
  }
})

def upload_store(store_name, store_area, store_status):
  with engine.connect() as conn:
      conn.execute(text("INSERT INTO Stores (Name, Area, Status, CenterName) VALUES (:name, :area, :status, 'Plaza Norte 2')"), 
                   {"name": store_name, "area": store_area, "status": store_status})

def delete_store(store_name):
  with engine.connect() as conn:
    store_id_row = conn.execute(text("SELECT ID FROM Stores WHERE Name = :name"), {"name": store_name}).fetchone()
    if store_id_row:
      store_id = store_id_row[0]
      # Delete the products of the store
      conn.execute(text("DELETE FROM Products WHERE StoreID = :id"), {"id": store_id})
      # Delete the store
      conn.execute(text("DELETE FROM Stores WHERE Name = :name"), {"name": store_name})
    else:
      # Handle the case where the store is not found
      print("Store not found")


def upload_product(product_name, product_price, product_store_name):
  with engine.connect() as conn:
      conn.execute(text("INSERT INTO Products (Name, Price, StoreID) VALUES (:name, :price, (SELECT ID FROM Stores WHERE Name = :store))"), 
                   {"name": product_name, "price": product_price, "store": product_store_name})

def delete_product(product_id):
  with engine.connect() as conn:
    conn.execute(text("DELETE FROM Products WHERE ID = :id"), {"id": product_id})

def load_stores():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Name FROM Stores"))

def load_products():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Products.ID, Products.Name FROM Products"))


# def load_employees_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM Employees"))
#     employees = []
#     for row in result.all():
#       employees.append(dict(row))
#     return employees

