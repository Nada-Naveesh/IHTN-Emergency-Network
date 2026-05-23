from flask import Flask
from flask_cors import CORS
from routes.emergency import emergency_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(emergency_bp)

@app.route("/")
def home():
    return {"message": "IHTN Backend Running on Render"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
