# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


# DEFINE THE DATABASE CREDENTIALS
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
db_connection_string,
connect_args={
  "ssl": {
    "ssl_ca": ""
    }
  },
  isolation_level="REPEATABLE READ"
)

Session = sessionmaker(bind=engine)

def upload_store(store_name, store_area, store_status): # ORM
  with Session.begin() as session:
    session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
    session.execute(text("INSERT INTO Stores (Name, Area, Status, CenterName) VALUES (:name, :area, :status, 'Plaza Norte 2')"), 
                   {"name": store_name, "area": store_area, "status": store_status})

def mod_store(store_name, store_area, store_status): # ORM
  with Session.begin() as session:
    session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
    session.execute(text("UPDATE Stores SET Area = :area, Status = :status WHERE Name = :name;"), 
                   {"name": store_name, "area": store_area, "status": store_status})

def delete_store(store_name): # ORM
  with Session.begin() as session:
    session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
    store_id_row = session.execute(text("SELECT ID FROM Stores WHERE Name = :name"), {"name": store_name}).fetchone()
    if store_id_row:
      store_id = store_id_row[0]
      # Delete the products of the store
      session.execute(text("DELETE FROM Products WHERE StoreID = :id"), {"id": store_id})
      # Delete the employees of that store
      session.execute(text("DELETE FROM StoreEmps WHERE StoreID = :id"), {"id": store_id})
      # Delete the store
      session.execute(text("DELETE FROM Stores WHERE Name = :name"), {"name": store_name})


def upload_product(product_name, product_price, product_store_name): # ORM # Req 7 
  with Session.begin() as session:
    try:
        session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
        session.execute(text("INSERT INTO Products (Name, Price, StoreID) VALUES (:name, :price, (SELECT ID FROM Stores WHERE Name = :store))"), 
                     {"name": product_name, "price": product_price, "store": product_store_name})
        return True
    except IntegrityError as e:
        if '1048' in str(e):
            return False
        else:
            raise e


def mod_product(product_id, product_name, product_price): # ORM
  with Session.begin() as session:
    # Check if the product exists
    session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
    product_row = session.execute(text("SELECT ID FROM Products WHERE ID = :id"), {"id": product_id}).fetchone()
    if product_row:
      # If the product exists, update it
      session.execute(text("UPDATE Products SET Name = :name, Price = :price WHERE ID = :id;"), 
                   {"id": product_id, "name": product_name, "price": product_price})
      return 'Product updated successfully'
    else:
      # If the product doesn't exist, return an error message
      return 'Integrity Error: Tried editing a product that was just removed from the mall by another user. Please go back and refresh the page.'


def delete_product(product_id): # ORM
  with Session.begin() as session:
    session.execute(text("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE"))
    session.execute(text("DELETE FROM Products WHERE ID = :id"), {"id": product_id})

def load_stores(): # ORM
  with Session.begin() as session:
    return session.execute(text("SELECT Name FROM Stores"))

def load_stores_report(): # Prepared statement
  with engine.begin() as conn:
    stmt = text("SELECT * FROM Stores")
    result = conn.execute(stmt)
    stores = [{"id": row[0], "name": row[1], "area": row[2], "status": row[3]} for row in result]
    return stores

def load_products(): # ORM
  with Session.begin() as session:
    return session.execute(text("SELECT Products.ID, Products.Name FROM Products"))

def load_products_report(): # Prepared statement
  with engine.begin() as conn:
    stmt = text("SELECT * FROM Products")
    result = conn.execute(stmt)
    keys = list(result.keys())  # Convert keys to a list
    products = [{keys[i]: value for i, value in enumerate(row)} for row in result]
    return products

def load_distinct_products(): # ORM
  with Session.begin() as session:
    return session.execute(text("SELECT DISTINCT Products.Name FROM Products"))

def fetch_product_info(product_name, product_info): # Prepared statement
  with engine.begin() as conn:
    # Existing functionality
    if "Stores" in product_info and "Price" in product_info and "Product ID" in product_info:
      stmt = text("SELECT Stores.Name, Products.Price, Products.ID FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name")
    elif "Stores" in product_info and "Price" in product_info:
      stmt = text("SELECT Stores.Name, Products.Price FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name")
    elif "Stores" in product_info and "Product ID" in product_info:
      stmt = text("SELECT Stores.Name, Products.ID FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name")
    elif "Stores" in product_info:
      stmt = text("SELECT Stores.Name FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name")
    else:
      # Replace 'Product ID' with 'ID'
      product_info = ['ID' if info == 'Product ID' else info for info in product_info]
      stmt = text("SELECT {} FROM Products WHERE Name = :name".format(", ".join(product_info)))
    result = conn.execute(stmt, {"name": product_name})
    info = [list(row) for row in result]  # Convert each tuple into a list

    # New functionality
    stmt_min_price = text("SELECT MIN(Price) FROM Products WHERE Name = :name")
    min_price_result = conn.execute(stmt_min_price, {"name": product_name})
    min_price = min_price_result.scalar()  # scalar() returns the first element of the first result or None
    stmt_avg_price = text("SELECT Stores.Name, AVG(Products.Price) FROM Stores JOIN Products ON Stores.ID = Products.StoreID WHERE Products.Name = :name GROUP BY Stores.Name")
    avg_price_result = conn.execute(stmt_avg_price, {"name": product_name})
    avg_prices = [{"Store": row[0], "Average Price": row[1]} for row in avg_price_result]

    return {"Info": info, "Minimum Price of the product at the mall": min_price, "Average Prices of the Product at Each Store": avg_prices}



def load_employees(): # Prepared statement
  with engine.begin() as conn:
    # Fetch center employees
    stmt = text("""
      SELECT Employees.Name, CentEmps.Occupation, Employees.Salary
      FROM Employees
      JOIN CentEmps ON Employees.ID = CentEmps.ID
    """)
    result = conn.execute(stmt)
    center_employees = [{"name": row[0], "occupation": row[1], "salary": row[2]} for row in result]

    # Fetch store employees
    stmt = text("""
      SELECT Employees.Name, StoreEmps.AssociatedStatus, Stores.Name, Employees.Salary
      FROM Employees
      JOIN StoreEmps ON Employees.ID = StoreEmps.ID
      JOIN Stores ON StoreEmps.StoreID = Stores.ID
    """)
    result = conn.execute(stmt)
    store_employees = [{"name": row[0], "associated_status": row[1], "store": row[2], "salary": row[3]} for row in result]

    return {"Center Employees": center_employees, "Store Employees": store_employees}


def load_center_employee_occupations(): # Prepared statement
  with engine.begin() as conn:
    stmt = text("SELECT Occupation, COUNT(*) FROM CentEmps GROUP BY Occupation")
    result = conn.execute(stmt)
    occupations = [{row[0]: row[1]} for row in result]
    return occupations

def load_store_employee_counts(): # Prepared statement
  with engine.begin() as conn:
    stmt = text("SELECT Stores.Name, COUNT(*) FROM StoreEmps JOIN Stores ON StoreEmps.StoreID = Stores.ID GROUP BY Stores.Name")
    result = conn.execute(stmt)
    employee_counts = [{row[0]: row[1]} for row in result]
    return employee_counts



