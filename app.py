from flask import Flask, render_template, request, flash

app = Flask (__name__)

app.secret_key = "ngeagtahatg3q"

@app.route("/hello")

def index():
    flash("Hello, what is your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + " great to meet you!")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)