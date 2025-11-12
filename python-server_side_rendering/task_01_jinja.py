from flask import Flask, render_template

app = Flask(__name__)

# Route principale
@app.route('/')
def home():
    return render_template('index.html')

# Page "About"
@app.route('/about')
def about():
    return render_template('about.html')

# Page "Contact"
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
