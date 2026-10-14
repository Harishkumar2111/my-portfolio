"""
Application entry point redirecting to main.py
Allows running the website using either:
    python main.py
or
    python app.py
"""
import os
import threading
from main import app, open_browser

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        threading.Timer(1.2, open_browser, args=[port]).start()
    app.run(host='127.0.0.1', port=port, debug=True)
