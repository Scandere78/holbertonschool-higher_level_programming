from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, category, price FROM Products')
            products = cursor.fetchall()
            return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error_message='Wrong source')
    
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')
    elif source == 'sql':
        products = read_sqlite('products.db')
    else:
        products = []

    # Filtrer par `product_id` si fourni
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found')
        
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
