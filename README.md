# MyTweets 🐦

**MyTweets** is a simple Django web application built as part of my learning journey with Django.  
The main goal of this project was to understand **Django basics** like forms, URLs, models, and templates, while also practicing backend skills.

---

## 📌 Project Purpose
I am a beginner in Django, and this project is just for learning and practicing:
- How **Django forms** work
- How to connect **URLs** to views
- How to create and use **models** with the database
- How to structure a basic Django project

For the frontend, I used **Bootstrap** to make the design clean and responsive.  
I already know **HTML**, **CSS**, and **JavaScript**, but Bootstrap made it easier to style without writing all CSS from scratch.

---

## ⚙️ Features
- **User Authentication** (Login required for certain actions)
- **Registration** system for new users
- **Login** with Django authentication (using `@login_required` decorator)
- Logged-in users can:
  - Post new tweets
  - Edit **only** their own tweets
  - Delete **only** their own tweets
- Users can view tweets from all other users but cannot edit or delete them
- Bootstrap styling for a clean and responsive interface

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default Django database for development)

---

## 🚀 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mytweets.git
