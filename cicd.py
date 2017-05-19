from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello world"


@app.route("/")
def index():
    entries = [
        { "text": "Hello" },
        { "text": "world" }
    ]
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run()
