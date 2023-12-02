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

@app.route('/user/new',)
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    User.add(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show_user.html", user=User.one_user(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html",user=User.one_user(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data={
        "id":id
    }
    user=User.remove(data)
    return redirect('/users')

if __name__ == '__main__' :
    app.run(debug='True')