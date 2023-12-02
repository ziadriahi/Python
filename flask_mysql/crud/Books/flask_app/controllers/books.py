from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app import app


@app.route('/books')
def books():
    return render_template("books.html",all_books=Book.get_all())

@app.route('/create/book',methods=['POST'])
def create_book():
    data=request.form
    Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data={
        "id" : id
    }
    return render_template("show_book.html",book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))


@app.route('/join/author',methods=['POST'])
def join_author():
    data={
        'author_id':request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Book.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")
