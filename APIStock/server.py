from flask import Flask, render_template
from api_handler import ApiHandler

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    ApiHandler.request_test()
    # app.run()

