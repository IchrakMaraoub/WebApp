from flask import Flask, render_template, request, redirect, url_for
from product_data import products
app = Flask(__name__)


# Existing route for displaying products
@app.route('/')
def index():
    # Cosmetic product data
    
    return render_template('index.html', products=products)

# New route for adding a product
@app.route('/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        price = request.form['price']

        # Assuming a simple incremental ID
        new_product = {'id': len(products) + 1, 'name': name, 'brand': brand, 'price': price}
        products.append(new_product)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
