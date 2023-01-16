from flask import Flask, render_template

app = Flask("My Blog")

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")

@app.route("/Skills")
def skills():
    return render_template("Skills.html")

@app.route("/Portfolio")
def portfolio():
    return render_template("Portfolio.html")

@app.route("/Contact")
def contact():
    return render_template("Contact.html")

app.run(port=131, debug=True)