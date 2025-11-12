from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


# New road /items
@app.route('/items')
def items():
    items_list = []

    # check if exist
    if os.path.exists('items.json'):
        try:
            with open('items.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier JSON : {e}")
    else:
        print("Le fichier items.json est introuvable.")

    # return the list to template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
