"""
Flask Development Guidelines for Junior Developers

These rules are designed to help you write safer, more maintainable Flask applications.
Follow these guidelines to avoid common pitfalls and security issues.
"""

# Rule 1: Always Validate and Sanitize User Input
"""
BAD:
@app.route('/user/<username>')
def user_profile(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"  # VULNERABLE!
    
GOOD:
from flask import request
from werkzeug.utils import escape

@app.route('/user/<username>')
def user_profile(username):
    # Sanitize input to prevent XSS
    safe_username = escape(username)
    # Use parameterized queries to prevent SQL injection
    user = db.session.query(User).filter_by(username=safe_username).first()
"""

# Rule 2: Use Environment Variables for Sensitive Configuration
"""
BAD:
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['DATABASE_URL'] = 'postgresql://user:password@localhost/db'

GOOD:
from os import environ
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['DATABASE_URL'] = environ.get('DATABASE_URL')
"""

# Rule 3: Always Handle Errors Appropriately
"""
BAD:
@app.route('/data')
def get_data():
    data = process_data()  # This might fail!
    return jsonify(data)

GOOD:
from flask import jsonify

@app.route('/data')
def get_data():
    try:
        data = process_data()
        return jsonify(data)
    except DatabaseError:
        return jsonify({'error': 'Database error occurred'}), 500
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception:
        # Log the unexpected error here
        return jsonify({'error': 'An unexpected error occurred'}), 500
"""

# Additional Tips:
# - Always use HTTPS in production
# - Keep your dependencies updated
# - Use Flask's built-in security features (e.g., csrf_token)
# - Write tests for your routes
# - Use blueprints to organize large applications 