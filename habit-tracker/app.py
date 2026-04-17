from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    habit_name = request.form["habit_name"]
    return f"You want to create: {habit_name}"

if __name__ == "__main__":
    app.run(debug=True)
