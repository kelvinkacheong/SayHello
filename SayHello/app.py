from flask import Flask, render_template, request, flash

app = Flask(__name__, template_folder="templates")
app.secret_key = "12344567"

@app.route("/hello")
def index():
    flash("Whats your name?")
    return render_template("home.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash(f"Hi {str(request.form['name_input'])}, great to see you! ")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)