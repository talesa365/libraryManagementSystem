from flask import Flask, request, render_template, redirect, url_for
from library import Library

app = Flask(__name__)
library = Library() #creates an instance of library

@app.route('/')
def index():
    books = library.get_all_books() #renders the list of books to index.html
    return render_template('index.html',books=books)#books=books allows us to access the variable
@app.route('/add', methods=['GET'])
def add():
    title = request.form.get('title')#input form with the name of 'title
    if title:
        return f"Book '{title}' added successfully!"
    else:
        return "No book title provided.", 400
    author = request.form.get('author')
    if title and author:
        library.add_books(title,author)
        return redirect(url_for('index'))
                    
@app.route('/delete/<int:book_id>')
def delete(book_id):
    library.delete_book(book_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)