from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<x>')
def alternate_squares(x):
    return render_template("alternate_squares.html", x = int(x), y = int(8))

if __name__ == "__main__":
    app.run()