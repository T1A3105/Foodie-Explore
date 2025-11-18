# Foodie-Explore
website designed for food enthusiasts to explore, share, and review various recipes and dining experiences. The website features user authentication, a recipe submission system, and an interactive rating and review system
This project is a basic web application created for learning and demonstration purposes.
It includes:

✔ User Login Page

✔ Login authentication using Flask sessions

✔ A homepage showing a list of recipes

✔ Each recipe includes description + user reviews

🗂️ Project Structure
foodie-website/
│
├── app.py
├── templates/
│     ├── login.html
│     └── recipes.html
└── static/
      └── styles.css

🚀 Features
🔐 1. User Login System

A login form (email + password).

Validates using a user stored in the backend.

Uses Flask session to maintain login.

🍕 2. Recipes Page

Shows a list of recipes.

Each recipe contains:

Title

Description

List of reviews (star rating + comment)

🎨 3.  UI

Designed using basic CSS.

Easy to modify for beginners.

🛠️ Technologies Used

Python Flask (Backend)

HTML (Frontend structure)

CSS (Styling)

Jinja2 templates (Rendering pages)

Flask session (Login state)

📚 Step-By-Step Implementation

✅ Step 1: Set up project folder

Created a folder and added:

app.py

templates/ folder

static/ folder

✅ Step 2: Installed Flask

Used the following command:

pip install flask

✅ Step 3: Built the Backend (app.py)

Implemented:

Flask server setup

Login route (/)

Recipe page route (/recipes)

Logout route (/logout)
 user data

List of recipes + reviews

Session-based authentication

✅ Step 4: Created Login Page (login.html)

Built a simple HTML form

Added fields for email & password

Displayed error message for wrong login

Connected form to backend using POST method

✅ Step 5: Created Recipes Page (recipes.html)

Displayed recipe name + description

Displayed reviews under each recipe

Used Jinja2 loops to dynamically show recipe data

Added logout button

✅ Step 6: Designed Page Styles (styles.css)

Styled containers

Form inputs and buttons

Recipe cards

Review section

Error and logout button styles

✅ Step 7: Tested End-to-End

Launched Flask server

Logged in with dummy credentials

Verified redirect to recipe page

Checked that reviews load correctly

▶️ How to Run This Project
1️⃣ Install Flask
pip install flask

2️⃣ Run the Flask app
python app.py

3️⃣ Open the app in browser
http://127.0.0.1:5000/
