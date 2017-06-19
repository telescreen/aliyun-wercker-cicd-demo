from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    entries = model_data()
    return render_template("index.html", entries=entries)

@app.route("/newlayout")
def newlayout():
    entries = model_data()
    return render_template("newlayout.html", entries=entries)

def model_data():
    return [
        { "text": "Hello world" },
        { "text": "From SBCloud!" },
        { "text": "Hello again!" }
    ]

if __name__ == "__main__":
    app.run()
