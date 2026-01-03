# app.py - Web Service Entry Point for Render
from flask import Flask
import threading
import os
from main import run_bot  # Import bot runner from main.py

# Create Flask app for health checks
app = Flask(__name__)

@app.route('/')
def health_check():
    return {
        "status": "running",
        "service": "telegram-bot",
        "message": "Bot is operational"
    }, 200

@app.route('/health')
def health():
    return "OK", 200

def run_web_server():
    """Run Flask on Render's port"""
    port = int(os.environ.get("PORT", 10000))
    print(f"🌐 Starting web server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    # Start Flask in background thread
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    
    # Run bot in main thread (IMPORTANT!)
    run_bot()
    
