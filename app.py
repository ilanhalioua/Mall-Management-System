from flask import Flask, render_template, request, jsonify
from database import upload_product, upload_stores #, load_employees_from_db

app = Flask(__name__)

@app.route("/")
def hello_mms():
  # employees = load_employees_from_db()
  return render_template('home.html')

@app.route("/add_product", methods=['POST'])
def add_product():
    product_name = request.form['product-name']
    product_price = request.form['product-price']
    product_store_name = request.form['store-name']
    upload_product(product_name, product_price, product_store_name)
    return 'Product added successfully'

@app.route("/get_stores", methods=['GET'])
def get_stores():
  result = upload_stores()
  stores = [row[0] for row in result]
  return jsonify(stores)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
