from flask import Flask,render_template,redirect,request,session
import random

app=Flask(__name__)
app.secret_key="1234"

@app.route('/')
def index():
    if "id" not in session:
        session['id']=random.randint(1,100)
    return render_template("index.html")

@app.route('/guess',methods=['POST'])
def guess():
    session['nbre']=int(request.form['nbre'])
    return redirect('/')

@app.route('/reset')
def resest():
    session.clear()
    return redirect('/')

if __name__ == "__main__" :
    app.run(debug="True")