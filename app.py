from flask import Flask
import os  # ← Add this import

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Tushar'

if __name__ == "__main__":
    # Get port from environment (Render sets this automatically)
    # Default to 5000 for local development
    port = int(os.environ.get("PORT", 5000))
    # Bind to 0.0.0.0 to accept external connections
    app.run(host='0.0.0.0', port=port)
    
