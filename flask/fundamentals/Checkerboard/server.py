from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def checkborder():
    color1='style=background-color:red;'
    color2='style=background-color:blue;'
    return render_template("index.html",x=8,y=8,color1=color1, color2=color2)

@app.route('/<int:x>')
def one_param(x):   
    color1='style=background-color:red;'
    color2='style=background-color:blue;'
    return render_template("index.html",x=x,y=8,color1=color1, color2=color2)

@app.route('/<int:x>/<int:y>')
def two_param(x,y):
    color1='style=background-color:red;'
    color2='style=background-color:blue;'
    return render_template("index.html",x=x ,y=y,color1=color1, color2=color2)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def four_param(x,y,color1,color2):
    color1=f'style=background-color:{color1};'
    color2=f'style=background-color:{color2};'
    return render_template("index.html",x=x ,y=y,color1=color1,color2=color2)

if __name__ =='__main__' :
    app.run(debug =True)