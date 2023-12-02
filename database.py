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

def mod_store(store_name, store_area, store_status):
  with engine.connect() as conn:
      conn.execute(text("UPDATE Stores SET Area = :area, Status = :status WHERE Name = :name;"), 
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

def mod_product(product_id, product_name, product_price):
  with engine.connect() as conn:
      conn.execute(text("UPDATE Products SET Name = :name, Price = :price WHERE ID = :id;"), 
                   {"id": product_id, "name": product_name, "price": product_price})

def delete_product(product_id):
  with engine.connect() as conn:
    conn.execute(text("DELETE FROM Products WHERE ID = :id"), {"id": product_id})

def load_stores():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Name FROM Stores"))

def load_products():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Products.ID, Products.Name FROM Products"))

def load_distinct_products():
  with engine.connect() as conn:
    return conn.execute(text("SELECT DISTINCT Products.Name FROM Products"))

def fetch_product_info(product_name, product_info):
  with engine.connect() as conn:
    # Existing functionality
    if "Stores" in product_info and "Price" in product_info and "Product ID" in product_info:
      query = "SELECT Stores.Name, Products.Price, Products.ID FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name"
    elif "Stores" in product_info and "Price" in product_info:
      query = "SELECT Stores.Name, Products.Price FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name"
    elif "Stores" in product_info and "Product ID" in product_info:
      query = "SELECT Stores.Name, Products.ID FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name"
    elif "Stores" in product_info:
      query = "SELECT Stores.Name FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name"
    else:
      query = "SELECT {} FROM Products WHERE Name = :name".format(", ".join(product_info))
    result = conn.execute(text(query), {"name": product_name})
    info = [list(row) for row in result]  # Convert each tuple into a list

    # New functionality
    min_price_result = conn.execute(text("SELECT MIN(Price) FROM Products WHERE Name = :name"), {"name": product_name})
    min_price = min_price_result.scalar()  # scalar() returns the first element of the first result or None
    avg_price_result = conn.execute(text("SELECT Stores.Name, AVG(Products.Price) FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name GROUP BY Stores.Name"), {"name": product_name})
    avg_prices = [{"Store": row[0], "Average Price": row[1]} for row in avg_price_result]

    return {"Info": info, "Minimum Price of the product at the mall": min_price, "Average Prices of the Product at Each Store": avg_prices}



# def load_employees_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM Employees"))
#     employees = []
#     for row in result.all():
#       employees.append(dict(row))
#     return employees

