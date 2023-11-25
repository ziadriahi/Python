from flask import Flask, render_template,request,redirect, session

app=Flask(__name__)
app.secret_key='1234'

@app.route('/')
def index():
    if "count" not in session:
        session["count"]=0
    else:
        session["count"]+=1
    return render_template('index.html')

@app.route('/increment')
def two_increment():
    session["count"]+=1
    return redirect('/')

@app.route('/reset')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/form_increment', methods=['POST'])
def spec_increment():
    session["count"] += int(request.form['nbre'])-1
    return redirect('/')

if __name__=='__main__':
    app.run(debug='True')