Travel has become a major part of life — for students, families, and friends.
While it’s easy to find information about places, hotels, and routes, travellers often struggle with what food to try in a new city or region.

This application fills that gap by offering a simple, interactive platform:

Explore popular dishes from different places

Read descriptions and traveller reviews

Share your own feedback

Make informed decisions about which dishes to try

It brings together recipe descriptions, reviews, and user interaction into one simple platform.

🎯 Key Features
✅ Travel-Based Food Exploration

Discover popular dishes by city or region

View detailed descriptions of each food item

✅ Reviews and Ratings

Read reviews posted by other travellers

Rate dishes from 1 to 5 stars

Decide which recipes are worth trying

✅ User Interaction

Post your own reviews for dishes you tried

Inspire other travellers with your feedback

Helps build a community of food explorers

🗂️ Project Structure
foodie-website/
│
├── app.py
├── templates/
│     ├── login.html
│     └── recipes.html
└── static/
      └── styles.css

🛠️ Technologies Used

Python Flask – Backend & routing

HTML – Page structure

CSS – Styling

Flask sessions – Login system

Jinja templates – Display dynamic food items & reviews

📘 Step-By-Step Implementation
Step 1: Identify a Real-Life Problem

Travellers often know where to go, but not what food to try.
The application was built to solve this gap.

Step 2: Set Up Flask Project

Created app.py for backend

Added templates/ and static/ folders

Step 3: Implement User Login

Simple login with email and password

Flask session for authentication

Step 4: Add Food Item Data

Each recipe includes:

Place name

Dish name

Description

Reviews & ratings

Step 5: Create Food Exploration Page

Display recipes by city

Show all reviews and ratings

Step 6: Add Review Submission

Users can submit their own reviews with a rating

Reviews are immediately visible to others

Makes the platform interactive and community-driven

Step 7: Style Pages with CSS

Clean and beginner-friendly UI

Step 8: Test Complete Flow

Login → Explore foods → Add review → Logout

▶️ How to Run This Project
1️⃣ Install Flask
pip install flask

2️⃣ Start the server
python app.py

3️⃣ Open in browser
http://127.0.0.1:5000

🔑 Default Login Credentials
Field	Value
Email	test@example.com

Password	1234
🗺️ Real Use-Cases

Travellers planning vacations: check famous food items before visiting

Students or solo travellers: discover popular dishes easily

Families: save time and travel cost while exploring food

Food enthusiasts: explore local dishes and share feedback

🚀 Future Enhancements

Add location filters to explore dishes by city/region

Connect to a real database (SQLite, MySQL)

Add image gallery for each dish

Include GPS-based nearby food recommendations

Allow multiple users with account creation

🏁 Conclusion

This application solves the gap in food exploration during travel.
It allows users to discover local dishes, read reviews, and post feedback — creating a complete travel food guide.
