# 📚 Library Management System

A simple Library Management System built with **Python, Django, SQLite, and Django ORM**.

This project manages books, members, and borrowing records using a database instead of Python lists and dictionaries.

## ✨ Features

* 📚 View all books
* 🔍 Search books by title or author
* ➕ Add new books
* ✏️ Edit books
* 🗑️ Delete books
* 👥 View members
* ➕ Add new members
* 📖 Borrow books
* ↩️ Return books
* 🚫 Prevent borrowing an unavailable book
* 📋 View member borrowing history
* 📊 View library statistics
* 🛠️ Manage books, members, and borrowings through Django Admin

## 🛠️ Technologies

* Python
* Django
* Django ORM
* SQLite
* HTML
* Tailwind CSS

## 📂 Project Structure


libraryProject/
│
├── library/
│   ├── migrations/
│   ├── templates/
│   │   └── library/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── db.sqlite3
└── README.md


## 🚀 Installation

Clone the project:


git clone <your-github-repository-url>
cd libraryProject


Create and activate a virtual environment:

### Windows


python -m venv .venv
.venv\Scripts\activate


Install Django:


pip install django


## 🗄️ Database Setup

Run migrations:


python manage.py makemigrations
python manage.py migrate


## 👤 Create Admin User

To access Django Admin:


python manage.py createsuperuser


Then follow the instructions in the terminal.

## ▶️ Run the Project

Start the development server:


python manage.py runserver


Open the project in your browser:


http://127.0.0.1:8000/


Django Admin:


http://127.0.0.1:8000/admin/


## 🗃️ Database Models

The project uses three Django models:

### Book

Stores:

* Title
* Author
* Publication year
* Availability
* Borrow count

### Member

Stores:

* Name
* Email

### Borrowing

Stores:

* Book
* Member
* Borrow date
* Return date

## 🔎 Search

Books can be searched by:

* Title
* Author

The search is implemented using Django ORM.

## 📖 Borrowing System

A member can borrow an available book.

When a book is borrowed:

* Its availability changes to unavailable.
* The borrow count increases.
* A borrowing record is saved in the database.

When the book is returned:

* Its availability changes back to available.
* The return date is saved in the borrowing record.

A book that is currently borrowed cannot be borrowed again.

## 📊 Statistics

The statistics page calculates information directly from the database, including:

* Total books
* Available books
* Borrowed books
* Total members
* Most borrowed book

## 📝 Notes

This project uses **SQLite** as the development database.

All books, members, and borrowing records are stored in the database using Django Models and Django ORM.

The project no longer depends on `sample_data.py` for its main data.


## 🔗 Repository

GitHub: https://github.com/zeinabgh1997/LibraryProject-task4
