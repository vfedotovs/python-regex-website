"""
app.py

A Flask web application for regex pattern matching.

This module implements a Flask application with proper configuration,
security measures, and error handling following best practices.

Example:
    $ flask run
    Or with python:
    $ python app.py

Attributes:
    app (Flask): The main Flask application object.

Routes:
    / (GET, POST): Regex pattern matching interface.
"""

import os
import re
import logging
from typing import Optional, List
from flask import Flask, render_template, request, flash, redirect, url_for, abort
from flask_wtf.csrf import CSRFProtect
from werkzeug.exceptions import BadRequest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app(test_config=None):
    """Application factory pattern for Flask best practices."""
    app = Flask(__name__)
    
    # Configuration
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production'),
        DEBUG=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true',
    )
    
    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.update(test_config)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize CSRF protection
    csrf = CSRFProtect(app)
    
    # Register routes
    app.register_blueprint(main_bp)
    
    return app

def validate_regex_pattern(pattern: str) -> bool:
    """Validate if the regex pattern is safe and valid."""
    if not pattern or len(pattern) > 1000:  # Reasonable length limit
        return False
    
    # Check for potentially dangerous patterns
    dangerous_patterns = [
        r'^.*$',  # Matches everything
        r'.*',    # Greedy matching
        r'(.+)\1+',  # Repeating groups
    ]
    
    for dangerous in dangerous_patterns:
        if pattern == dangerous:
            return False
    
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def safe_regex_findall(pattern: str, text: str) -> List[str]:
    """Safely perform regex findall operation with proper error handling."""
    if not validate_regex_pattern(pattern):
        raise ValueError("Invalid or unsafe regex pattern")
    
    if not text or len(text) > 10000:  # Reasonable text length limit
        raise ValueError("Text too long or empty")
    
    try:
        matches = re.findall(pattern, text)
        return matches if matches else []
    except re.error as e:
        logger.warning(f"Regex error: {e} for pattern: {pattern}")
        raise ValueError(f"Regex compilation error: {str(e)}")

# Blueprint for main routes
from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    """Handle regex pattern matching requests."""
    regex_result = ""
    error_message = ""
    
    if request.method == "POST":
        try:
            pattern = request.form.get("pattern", "").strip()
            text = request.form.get("text", "").strip()
            
            # Input validation
            if not pattern:
                raise ValueError("Regex pattern is required")
            if not text:
                raise ValueError("Text to search is required")
            
            # Perform regex matching
            matches = safe_regex_findall(pattern, text)
            regex_result = ", ".join(matches) if matches else "No matches found"
            
            logger.info(f"Successful regex match: pattern='{pattern}', matches={len(matches)}")
            
        except ValueError as e:
            error_message = str(e)
            logger.warning(f"Validation error: {error_message}")
        except Exception as e:
            error_message = "An unexpected error occurred. Please try again."
            logger.error(f"Unexpected error in regex matching: {e}")
    
    return render_template(
        "index.html", 
        regex_result=regex_result, 
        error_message=error_message
    )

@main_bp.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    return render_template("error.html", error="Bad Request"), 400

@main_bp.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return render_template("error.html", error="Page Not Found"), 404

@main_bp.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return render_template("error.html", error="Internal Server Error"), 500

# Create the app instance
app = create_app()

if __name__ == "__main__":
    # Use environment variables for configuration
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)
