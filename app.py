from flask import Flask, render_template, request, flash

app = Flask (__name__)

app.secret_key = "ngeagtahatg3q"

@app.route("/hello")

# Render the initial page
def index():
    flash("Hello, what is your name?")
    return render_template("index.html")

# Re-route the user once the have entered their name and pressed the "Greet" button
@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + " great to meet you!")
    return render_template("index.html")

# For testing only
if __name__ == '__main__':
    app.run(debug=True, port=8000)