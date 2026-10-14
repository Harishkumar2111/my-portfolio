import os
import sys
import json
import webbrowser
import threading
from datetime import datetime, timezone
from flask import Flask, render_template, send_from_directory, request, jsonify, abort

# Ensure UTF-8 console output on Windows

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(BASE_DIR, 'templates')
static_folder = os.path.join(BASE_DIR, 'static')

app = Flask(
    __name__,
    template_folder=template_folder,
    static_folder=static_folder
)

# Configuration
RESUME_FILENAME = 'Harish_Kumar_Resume.pdf'
FILES_DIR = os.path.join(static_folder, 'files')
MESSAGES_FILE = os.path.join(BASE_DIR, 'messages.json')

@app.route('/')
def home():
    """Serve the main portfolio homepage."""
    return render_template('index.html')

@app.route('/download-resume')
def download_resume():
    """Securely serve and trigger download of Harish's official resume PDF."""
    try:
        resume_path = os.path.join(FILES_DIR, RESUME_FILENAME)
        if not os.path.exists(resume_path):
            return abort(404, description="Resume file not found on server.")
        return send_from_directory(
            FILES_DIR,
            RESUME_FILENAME,
            as_attachment=True,
            download_name='Harish_Kumar_Resume.pdf',
            mimetype='application/pdf'
        )
    except Exception as e:
        return abort(500, description=str(e))

@app.route('/view-resume')
def view_resume():
    """Serve the resume PDF inline for interactive browser viewing."""
    try:
        resume_path = os.path.join(FILES_DIR, RESUME_FILENAME)
        if not os.path.exists(resume_path):
            return abort(404, description="Resume file not found on server.")
        return send_from_directory(
            FILES_DIR,
            RESUME_FILENAME,
            as_attachment=False,
            mimetype='application/pdf'
        )
    except Exception as e:
        return abort(500, description=str(e))

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submission, validate inputs, and store safely."""
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', 'New Contact Form Submission').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return jsonify({
                'success': False,
                'message': 'Please fill in all required fields (Name, Email, Message).'
            }), 400

        entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'ip': request.remote_addr
        }

        # Save message to local messages.json
        messages = []
        if os.path.exists(MESSAGES_FILE):
            try:
                with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
                    messages = json.load(f)
            except Exception:
                messages = []

        messages.append(entry)
        with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)

        return jsonify({
            'success': True,
            'message': f'Thank you, {name}! Your message has been received successfully.'
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Graceful 404 handler rendering home."""
    return render_template('index.html'), 404

def open_browser(port):
    """Optionally open the default browser once the server is ready."""
    try:
        webbrowser.open(f'http://127.0.0.1:{port}')
    except Exception:
        pass

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("\n=======================================================")
    print("   HARISH K. M - PORTFOLIO WEB APPLICATION SERVER    ")
    print("=======================================================")
    print(f"[*] Main Server Script: main.py")
    print(f"[*] Access Website:     http://127.0.0.1:{port}")
    print(f"[*] Resume Download:    http://127.0.0.1:{port}/download-resume")
    print(f"[*] Resume View:        http://127.0.0.1:{port}/view-resume")
    print("=======================================================\n")
    
    # Auto-open browser in non-reloader mode
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        threading.Timer(1.2, open_browser, args=[port]).start()

    app.run(host='127.0.0.1', port=port, debug=True)
