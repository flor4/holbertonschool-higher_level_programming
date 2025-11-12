from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


# Function that read JSON data
def read_json(file_path='products.json'):
    with open(file_path, 'r') as f:
        return json.load(f)


# Function that read CSV data
def read_csv(file_path='products.csv'):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    # check the source
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source", products=None)

    # read the data
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # Filter
    if id_param:
        try:
            id_int = int(id_param)
        except ValueError:
            return render_template('product_display.html', error="Invalid id parameter", products=None)

        data = [item for item in data if item['id'] == id_int]
        if not data:
            return render_template('product_display.html', error="Product not found", products=None)

    return render_template('product_display.html', products=data, error=None)


if __name__ == "__main__":
    app.run(debug=True)
