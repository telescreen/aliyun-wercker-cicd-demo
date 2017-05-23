from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    entries = model_data()
    return render_template("index.html", entries=entries)

def model_data():
    return [
        { "text": "Hello" },
        { "text": "world" },
        { "text": "one more" }        
    ]

if __name__ == "__main__":
    app.run()
