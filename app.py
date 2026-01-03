from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "OK"

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)
