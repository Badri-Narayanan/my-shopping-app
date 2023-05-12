from flask import Flask

app = Flask(__name__)


@app.route("/")
def dashboard_page():
    return "<h1> Welcome to my Shopping page!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
