from flask import Flask, render_template, request, jsonify, url_for

from chat import get_response, initialize

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.post("/predict")
def predict():
    INTENTS_PATH = url_for('static', filename='data/intents.json')
    DATA_PATH = url_for('static', filename='data/data.pth')
    initialize(DATA_PATH, INTENTS_PATH)
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
