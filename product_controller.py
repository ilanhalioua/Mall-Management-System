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
  
def update(args):
  with engine.connect() as conn:
    conn.execute(text(f"INSERT INTO Products SET Name = %s, Price = input_ProdPrice, StoreID = (SELECT ID FROM Stores WHERE Name = input_ProdStore));"))
    # print(result.all())