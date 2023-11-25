from flask import Flask,render_template, redirect, request

from users import User

app=Flask('__name__')

@app.route('/')
def home():
    return redirect('/users')

@app.route('/users')
def users():
    users= User.get_all()
    return render_template("users.html",users=users)

@app.route('/new',)
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.add(request.form)
    return redirect('/users')


if __name__ == '__main__' :
    app.run(debug='True')