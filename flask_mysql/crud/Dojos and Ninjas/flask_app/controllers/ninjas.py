from flask import render_template,redirect,request
from flask_app.models import dojo,ninja
from flask_app import app 

@app.route('/ninjas')
def ninjas():
    dojos=dojo.Dojo.all_dojos()
    print(dojos)
    return render_template('ninja.html',dojos=dojos)

@app.route('/create/ninja',methods=['POST'])
def create():
    ninja.Ninja.create(request.form)
    return redirect('/')