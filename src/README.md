# Regex Matcher Flask Application

A secure and well-structured Flask web application for regex pattern matching, following Flask best practices.

## Features

- **Secure regex pattern matching** with input validation
- **CSRF protection** for all forms
- **Proper error handling** with user-friendly messages
- **Application factory pattern** for scalability
- **Environment-based configuration**
- **Comprehensive logging**
- **Responsive Bootstrap UI**

## Best Practices Implemented

### 1. **Security**
- ✅ CSRF protection with Flask-WTF
- ✅ Input validation and sanitization
- ✅ Regex pattern safety checks
- ✅ Environment variable configuration
- ✅ Secure default settings

### 2. **Code Structure**
- ✅ Application factory pattern
- ✅ Blueprint organization
- ✅ Proper separation of concerns
- ✅ Type hints for better code clarity
- ✅ Comprehensive error handling

### 3. **Configuration Management**
- ✅ Environment-based configuration
- ✅ Separate config classes for different environments
- ✅ Secure secret key management
- ✅ Debug mode control via environment variables

### 4. **Error Handling**
- ✅ Custom error handlers for HTTP status codes
- ✅ User-friendly error messages
- ✅ Proper logging of errors
- ✅ Graceful degradation

### 5. **User Experience**
- ✅ Responsive Bootstrap UI
- ✅ Clear error and success messages
- ✅ Example regex patterns
- ✅ Form validation feedback

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   export SECRET_KEY=your-super-secret-key
   ```

3. **Run the application:**
   ```bash
   flask run
   # or
   python app.py
   ```

## Environment Variables

Create a `.env` file with the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_HOST=127.0.0.1
FLASK_PORT=5000
SECRET_KEY=your-super-secret-key-change-this-in-production
```

## Project Structure

```
src/
├── app.py              # Main application file
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── index.html     # Main page template
│   └── error.html     # Error page template
└── README.md          # This file
```

## Security Features

- **Input Validation**: All user inputs are validated before processing
- **Regex Safety**: Dangerous regex patterns are blocked
- **CSRF Protection**: All forms include CSRF tokens
- **Error Handling**: Sensitive information is not exposed in error messages
- **Logging**: Security events are logged for monitoring

## API Endpoints

- `GET /` - Display the regex matching form
- `POST /` - Process regex pattern matching

## Error Codes

- `400` - Bad Request (invalid input)
- `404` - Page Not Found
- `500` - Internal Server Error

## Contributing

1. Follow PEP 8 style guidelines
2. Add type hints to new functions
3. Include proper error handling
4. Update documentation for new features
5. Test thoroughly before submitting

## License

This project is open source and available under the MIT License. 