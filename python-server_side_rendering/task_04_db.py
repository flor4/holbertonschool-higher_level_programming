from flask import Flask, render_template, request
import json, csv, sqlite3, os

app = Flask(__name__)

def read_json():
    try:
        with open('data/products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return {'error': f'Erreur JSON : {e}'}

def read_csv():
    products = []
    try:
        with open('data/products.csv', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append(row)
    except Exception as e:
        return {'error': f'Erreur CSV : {e}'}
    return products

def read_sqlite():
    try:
        db_path = os.path.join('data', 'products.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception as e:
        return {'error': f'Erreur SQL : {e}'}

@app.route('/')
def display_products():
    source = request.args.get('source', 'json').lower()

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sqlite()
    else:
        return render_template('product_display.html', error="Wrong source")

    if isinstance(data, dict) and 'error' in data:
        return render_template('product_display.html', error=data['error'])

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
