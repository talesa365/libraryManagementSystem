# Simple Library Management App
Talesa Howell

This is a basic Flask application that simulates a simple library management system. 

**Key Features:**

* Add new books to the library.
* View a list of all books in the library.
* Borrow books (marks the book as unavailable).
* Delete existing books from the library.

**Getting Started:**

1. **Project Setup:**
   - Create a new directory for the project (e.g., `library_app`).
   - Open a terminal and navigate to the project directory.
   - Create a virtual environment: `python3 -m venv venv` 
   - Activate the virtual environment:
      - **On macOS/Linux:** `source venv/bin/activate`
      - **On Windows:** `venv\Scripts\activate`

2. **Install Dependencies:**
   - Install Flask and Jinja2: `pip install Flask Jinja2`

3. **Project Structure:**
   - The project will have the following files:
      - `app.py`: The main Flask application file.
      - `library.py`: Contains the `Book` and `Library` classes.
      - `index.html`: The HTML template for the user interface.
