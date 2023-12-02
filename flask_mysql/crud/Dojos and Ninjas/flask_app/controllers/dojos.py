from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app import app 

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.all_dojos()
    return render_template('index.html',dojos=dojos)

@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.create(request.form)

    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data={
        "id":id
    }
    return render_template('dojo.html',dojo=Dojo.ninja_by_dojos_id(data))



