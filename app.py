from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "simple-secret"


USER = {
    "email": "test@example.com",
    "password": "1234"
}


RECIPES = [
    {
        "title": "Spaghetti",
        "description": "Italian style pasta.",
        "reviews": [
            {"user": "Alice", "comment": "Loved it!", "rating": 5},
            {"user": "Bob", "comment": "Pretty good.", "rating": 4}
        ]
    },
    {
        "title": "Paneer Butter Masala",
        "description": "Creamy North Indian curry.",
        "reviews": [
            {"user": "Rahul", "comment": "Amazing taste!", "rating": 5}
        ]
    }
]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == USER["email"] and password == USER["password"]:
            session["user"] = email
            return redirect("/recipes")
        else:
            return render_template("login.html", error="Invalid Credentials")
        
    return render_template("login.html")


@app.route("/recipes")
def recipes():
    if "user" not in session:
        return redirect("/")
    return render_template("recipes.html", recipes=RECIPES)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
