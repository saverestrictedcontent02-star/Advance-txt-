from flask import Flask
import os
import threading
import main  # main.py import

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Flask server thread (PORT ke liye)
    threading.Thread(target=run_flask).start()

    # Bot already runs because main.py ke end me bot.run() hai
    # Yahan kuch call karne ki zarurat nahi
