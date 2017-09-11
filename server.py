from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key = "badonkadonk"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    valid = True
    if len(request.form['name']) < 1:
        flash("*Name cannot be empty.")
        valid = False
    if len(request.form['comment']) < 1:
        flash("*Comment cannot be empty.")
        valid = False
    if len(request.form['comment']) > 120:
        flash("*Comment cannot be longer than 120 characters.")
        valid = False
    if valid:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['favoritelanguage'] = request.form['favoritelanguage']
        session['comment'] = request.form['comment']
        return redirect('/result')
    else:
        return redirect('/')

@app.route("/result")
def result():
    return render_template('result.html', name=session['name'], location=session['location'], favoritelanguage=session['favoritelanguage'], comment=session['comment'] )
    

app.run(debug=True)