from waitress import serve
from web.app import app  # Import the Flask application from the 'web' package

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
