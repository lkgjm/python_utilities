from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>")
def welcome(name):
    return render_template("welcome.html", name=name)


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    seasons = {"winter": "cold", "spring": "days longer", "summer": "hot", "autumn": "beautiful"}
    return render_template("about.html", seasons=seasons)


@app.route("/contact/<role>")
def contact(role):
    return render_template("contact.html", person=role)

if __name__ == "__main__":
    app.run(debug=True)