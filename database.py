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

def load_stores_report():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Stores"))
    stores = [{"id": row[0], "name": row[1], "area": row[2], "status": row[3]} for row in result]
    return stores

def load_products():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Products.ID, Products.Name FROM Products"))

def load_products_report():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Products"))
    keys = list(result.keys())  # Convert keys to a list
    products = [{keys[i]: value for i, value in enumerate(row)} for row in result]
    return products

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


def load_employees():
  with engine.connect() as conn:
    # Fetch center employees
    result = conn.execute(text("""
      SELECT Employees.Name, CentEmps.Occupation, Employees.Salary
      FROM Employees
      JOIN CentEmps ON Employees.ID = CentEmps.ID
    """))
    center_employees = [{"name": row[0], "occupation": row[1], "salary": row[2]} for row in result]

    # Fetch store employees
    result = conn.execute(text("""
      SELECT Employees.Name, StoreEmps.AssociatedStatus, Stores.Name, Employees.Salary
      FROM Employees
      JOIN StoreEmps ON Employees.ID = StoreEmps.ID
      JOIN Stores ON StoreEmps.StoreID = Stores.ID
    """))
    store_employees = [{"name": row[0], "associated_status": row[1], "store": row[2], "salary": row[3]} for row in result]

    return {"Center Employees": center_employees, "Store Employees": store_employees}


def load_center_employee_occupations():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Occupation, COUNT(*) FROM CentEmps GROUP BY Occupation"))
    occupations = [{row[0]: row[1]} for row in result]
    return occupations

def load_store_employee_counts():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT Stores.Name, COUNT(*) FROM StoreEmps JOIN Stores ON StoreEmps.StoreID = Stores.ID GROUP BY Stores.Name"))
    employee_counts = [{row[0]: row[1]} for row in result]
    return employee_counts



