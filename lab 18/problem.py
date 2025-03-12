from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    cars = [
        {"id": 1, "model": "Tesla Model S", "brand": "Tesla"},
        {"id": 2, "model": "Mustang", "brand": "Ford"},
        {"id": 3, "model": "Civic", "brand": "Honda"}
    ]
    return render_template('index.html', cars=cars, title="Car List")

if __name__ == '__main__':
    app.run(debug=True)
