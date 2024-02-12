from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/page2")
def page():
    return render_template("page2.html", bonjour = "Bella raga !")

app.run()