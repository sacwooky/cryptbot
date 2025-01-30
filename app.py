from flask import Flask, render_template
import logging

app = Flask(__name__)

# Example data
bot_status = "Running"
token_data = [
    {"name": "Token A", "price": "$1.00", "volume": "$100,000"},
    {"name": "Token B", "price": "$0.50", "volume": "$50,000"},
]

@app.route("/")
def home():
    return render_template("index.html", status=bot_status, tokens=token_data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=5000)