from flask import Flask, request, render_template, redirect, url_for
from library import Library #this imports all the neccessary tools from the Flask library

app = Flask(__name__) #this creates a Flask object nammed 'app', and name is a special variable, it tells Flask the name of the current Python file
library = Library() #creates an instance of library class defined in library.py (it creates a virtual library)

app.secret_key = "Abc123" #the secret key is used for security features from Flask (like flash)

@app.route('/') #defines a 'route' for the main page of the application

def index(): #this function is called when someone visits the (./.) root url of the application
    books = library.get_all_books() #renders the list of books to index.html
    return render_template('index.html',books=books)#books=books allows us to access the variable

@app.route('/add', methods=['POST']) #defines a route for the add book functionality, the POST request is used to submit data from the form

def add():#this is the logic to add books when a user submits the form
    title = request.form.POST('title')#input form with the name of 'title
    if title:
        return f"Book '{title}' added successfully!"
    else:
        return "No book title provided.", 400
    author = request.form.get('author')
    if title and author:
        library.add_books(title,author)
        return redirect(url_for('index'))
                    
@app.route('/delete/<int:book_id>')#defines a route for deleting a book
def delete(book_id):
    library.delete_book(book_id)
    return redirect(url_for('index'))

@app.route('/borrow/<int:book_id>') # indicates the the book_id is in the url and is an integer
def borrow_book(book_id):
    library.borrow_book(book_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)