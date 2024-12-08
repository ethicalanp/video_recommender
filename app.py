from flask import Flask
from feed import feed_bp
from api_services import fetch_user_interactions
app = Flask(__name__)
app.register_blueprint(feed_bp)


@app.route('/')
def home():
    return "Welcome to the Video Recommendation Service."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
