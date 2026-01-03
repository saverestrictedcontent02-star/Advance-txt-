from flask import Flask
import os
import threading
import main  # main.py jisme bot.run() hai

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

def run_bot():
    # bot.run() main.py ke end me already hai
    # sirf import kaafi hai, but safe call ke liye
    pass

if __name__ == "__main__":
    # 🔥 FIRST: Flask must start immediately
    port = int(os.environ.get("PORT", 10000))
    threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=port),
        daemon=True
    ).start()

    # 🔥 SECOND: Start Telegram bot (blocking)
    main.bot.run()
