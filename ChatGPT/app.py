from flask import Flask, redirect, render_template, request, url_for
from ai import AI

app = Flask(__name__)
website_ai = AI()

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        q = request.form["question"]
        response = website_ai.answer_question(question=q)
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)
