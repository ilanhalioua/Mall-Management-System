from flask import Flask, render_template, request, jsonify
from database import load_distinct_products, upload_product, load_stores, load_products, upload_store, mod_store, delete_store, delete_product, fetch_product_info, load_distinct_products #, mod_product, load_employees_from_db

app = Flask(__name__)

@app.route("/")
def hello_mms():
  # employees = load_employees_from_db()
  return render_template('home.html')


@app.route("/add_store", methods=['POST'])
def add_store():
    store_name = request.form['store-name']
    store_area = request.form['store-area']
    store_status = request.form['store-status']
    upload_store(store_name, store_area, store_status)
    return 'Store added successfully'

@app.route("/edit_store", methods=['POST'])
def edit_store():
    store_name = request.form['store-name']
    store_area = request.form['store-area']
    store_status = request.form['store-status']
    mod_store(store_name, store_area, store_status)
    return 'Store edited successfully'

@app.route("/remove_store", methods=['POST'])
def remove_store():
    store_name = request.form['store-name']
    delete_store(store_name)
    return 'Store removed successfully'


@app.route("/add_product", methods=['POST'])
def add_product():
    product_name = request.form['product-name']
    product_price = request.form['product-price']
    product_store_name = request.form['store-name']
    upload_product(product_name, product_price, product_store_name)
    return 'Product added successfully'

# @app.route("/edit_product", methods=['POST'])
# def edit_product():
#     product_id = request.form['product-id']
#     product_name = request.form['product-name']
#     product_price = request.form['product-price']
#     mod_product(product_id, product_name, product_price)
#     return 'Product edited successfully'

@app.route("/remove_product", methods=['POST'])
def remove_product():
    product_id = request.form['product-id']
    delete_product(product_id)
    return 'Product removed successfully'


@app.route("/search_product", methods=['POST'])
def search_product():
  product_name = request.form['product-name']
  product_info = request.form.getlist('product-info')
  result = fetch_product_info(product_name, product_info)
  return jsonify(result)

@app.route("/get_stores", methods=['GET'])
def get_stores():
  result = load_stores()
  stores = [row[0] for row in result]
  return jsonify(stores)

@app.route("/get_products", methods=['GET'])
def get_products():
  result = load_products()
  products = [{"id": row[0], "name": row[1]} for row in result]
  return jsonify(products)

@app.route("/get_distinct_products", methods=['GET'])
def get_distinct_products():
  result = load_distinct_products()
  products = [row[0] for row in result]
  return jsonify(products)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
