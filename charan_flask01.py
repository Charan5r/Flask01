from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/hello")
def home():
    return "Hello......Id no:%s...Please don't Waste"

@app.route("/charan/")
def second():
    return "Charan"


if __name__ == '__main__':
    app.run(debug=True)