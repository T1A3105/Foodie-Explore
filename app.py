from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "simple-secret"   # for sessions

# Simple user for login
USER = {
    "email": "test@example.com",
    "password": "1234"
}

# Travel-based food exploration data
RECIPES = [
    {
        "place": "Hyderabad",
        "title": "Hyderabadi Biryani",
        "description": "A world-famous aromatic biryani known for rich spices and dum-style cooking.",
        "reviews": [
            {"user": "Kiran", "comment": "A must-try in Hyderabad!", "rating": 5},
            {"user": "Sana", "comment": "Very flavorful, totally recommend.", "rating": 5}
        ]
    },
    {
        "place": "Mumbai",
        "title": "Vada Pav",
        "description": "Mumbai’s iconic street food – spicy, crispy, and budget-friendly.",
        "reviews": [
            {"user": "Ayesha", "comment": "Perfect snack while travelling!", "rating": 4}
        ]
    },
    {
        "place": "Amritsar",
        "title": "Amritsari Kulcha",
        "description": "Crispy, stuffed kulchas served with tangy chole, famous in Punjab.",
        "reviews": [
            {"user": "Rohit", "comment": "Amazing taste and authentic flavour.", "rating": 5}
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
            return redirect("/foods")
        else:
            return render_template("login.html", error="Invalid Credentials")
    return render_template("login.html")


@app.route("/foods", methods=["GET", "POST"])
def recipes():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        recipe_index = int(request.form.get("recipe_index"))
        comment = request.form.get("comment")
        rating = int(request.form.get("rating"))
        username = session["user"]
        
        # Add new review to the recipe
        RECIPES[recipe_index]["reviews"].append({
            "user": username,
            "comment": comment,
            "rating": rating
        })

    return render_template("recipes.html", recipes=RECIPES)


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
