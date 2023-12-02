from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app import app

@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("authors.html",all_authors=Author.get_all())

@app.route('/create/author',methods=['POST'])
def create_author():
    Author.save_author(request.form)
    return redirect('/authors')

@app.route('/author/<int:id>')
def show_author(id):
    data={
        "id" : id
    }
    return render_template("show_author.html",author=Author.get_by_id(data),unfavorite_books=Book.unfavorited_books(data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data={
        'author_id':request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")

