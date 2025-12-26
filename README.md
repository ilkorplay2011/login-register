# Flask Login & Registration

Simple Flask application with user registration and login.  
User data is stored in a JSON file.

⚠️ Educational project. Passwords are stored in plain text.

---

## Features

- User registration
- User login
- JSON-based storage
- HTML + CSS frontend

---

## Project Structure

project/
├── app.py
├── pass_and_us.json
├── templates/
│ ├── index.html
│ └── reg.html
├── static/
│ └── style.css
└── README.md
---

## Installation & Run

```bash
pip install flask
Create pass_and_us.json:

json
{}
Run the app:

bash
python app.py
Open in browser:

cpp
http://127.0.0.1:5000/
Routes
/ — Login page

/register — Registration page

Notes
No password hashing

No validation

No sessions

For learning purposes only

Author
ilia korkiti
