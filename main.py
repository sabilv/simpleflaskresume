from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"


@app.route("/homepage")
def homepage():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True)