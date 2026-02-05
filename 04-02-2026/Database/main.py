from flask import Flask
from API.login import auth_bp

app = Flask(__name__)

# Register blueprint
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
