from flask import Flask;

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return "Hello World!"

@app.route('/dojo')
def Dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def Say(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:str>')
def Repeat(num,str):
    return f"{str * num}"

if __name__ == "__main__":
    app.run(debug=True)