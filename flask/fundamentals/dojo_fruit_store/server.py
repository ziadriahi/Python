from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fruit=request.form.to_dict(flat=False)
    count=0
    for x, val in fruit.items():
        if (x == 'strawberry') or (x == 'raspberry') or (x == 'apple') :
            count+= int(val[0])
    
    for x, val in fruit.items():
        if (x == 'first_name'):
            first=val[0]
    
    for x, val in fruit.items():
        if (x == 'last_name'):
            last=val[0]
    
    for x, val in fruit.items():
        if (x == 'student_id'):
            id=val[0]

    print(f'Charging {first} {last} for {count} fruits')
    return render_template("checkout.html",fruit=fruit, count=count,first=first,last=last,id=id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    