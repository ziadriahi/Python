from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/play')
def play_levelone():
    return render_template("index.html",num=6, color="blue")

@app.route('/play/<int:num>')
def play_leveltwo(num):
    return render_template("index.html",num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def play_levelthree(num, color):
    color = f'style=background-color:{color};'
    return render_template("index.html",num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)