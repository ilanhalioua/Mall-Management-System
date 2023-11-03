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

def upload_product(product_name, product_price, product_store_name):
  with engine.connect() as conn:
      conn.execute(text("INSERT INTO Products (Name, Price, StoreID) VALUES (:name, :price, (SELECT ID FROM Stores WHERE Name = :store))"), 
                   {"name": product_name, "price": product_price, "store": product_store_name})


def upload_stores():
  with engine.connect() as conn:
    return conn.execute(text("SELECT Name FROM Stores"))


# def load_employees_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM Employees"))
#     employees = []
#     for row in result.all():
#       employees.append(dict(row))
#     return employees

