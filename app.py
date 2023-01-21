from flask import Flask, render_template
import blogAPI as blog

app = Flask("My Blog")

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/aboutMe")
def aboutMe():
    return render_template("aboutMe.html")

@app.route("/Resume")
def skills():
    return render_template("Resume.html")

@app.route("/Portfolio")
def portfolio():
    return render_template("Portfolio.html")

@app.route("/Contact")
def contact():
    res = blog.api()
    return render_template("Contact.html", list=res)

app.run(port=131, debug=True)