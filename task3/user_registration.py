from user import User
import sqlite3
import smtplib
from email.mime.text import MIMEText


def add_user(db, user: User) -> None:
    """Add a new user to the database and send message to his email"""
    try:
        with sqlite3.connect(db) as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO users (first_name, surname, last_name, email, age) VALUES (?, ?, ?, ?, ?)",
                (user.first_name, user.surname, user.last_name, user.email, user.get_age())
            )
            print("User added successfully")
    except sqlite3.Error as e:
        print(e)

    send_email(user.email)


def show_users(db) -> None:
    """Display all users in the database"""
    try:
        with sqlite3.connect(db) as conn:
            c = conn.cursor()
            result = c.execute("SELECT * FROM users").fetchall()
            for row in result:
                print(row)
    except sqlite3.Error as e:
        print(e)


def find_user(db, name: str, last_name: str, email: str) -> None:
    """Find a user in the database"""
    try:
        with sqlite3.connect(db) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE first_name = ? AND last_name = ? AND email = ?",
                      (name, last_name, email))
            rows = c.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def send_email(user_email: str) -> None:
    """Send a message to the user email"""
    sender = "pythonfortask@gmail.com"
    message = MIMEText("Hi! Thank you for registering!")
    message["Subject"] = "Registering your account!"
    message["From"] = sender
    message["To"] = user_email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, "mwgc otyf qytj hqqz")
        smtp_server.sendmail(sender, user_email, message.as_string())
    print("Email sent!")
