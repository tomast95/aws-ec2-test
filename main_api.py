import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f"Web App with Python Flask! .env file test variable is: {os.getenv('TEST_VAR', '-')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
