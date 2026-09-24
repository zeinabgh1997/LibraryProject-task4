# Library Management System

A simple library management system built with Django.

## Features

* View books and members
* Search books by title or author
* Borrow and return books
* Add new books
* View borrowing history
* View library statistics
* Uses sample data stored in Python lists and dictionaries
* No database or Django models are used

## Installation

1. Clone the repository:

git clone <repository-url>
cd libraryProject


2. Create and activate a virtual environment:

python -m venv .venv

Windows PowerShell:

powershell
.\.venv\Scripts\activate


3. Install the required packages:

pip install -r requirements.txt


## Run the Project

Start the Django development server:


python manage.py runserver


Then open the address shown in the terminal in your browser.

## Project Structure

* `manage.py` — Django management script
* `config/` — Django project configuration
* `library/` — main library application
* `library/templates/` — HTML templates
* `library/sample_data.py` — sample books, members, and borrowing data
* `requirements.txt` — project dependencies

## Data

This project uses sample data stored in Python lists and dictionaries in memory. No database, Django models, migrations, or admin panel are required.
