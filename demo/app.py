#!/usr/bin/env python3
from flask import Flask
from flask import render_template , request , redirect , url_for
app = Flask(__name__)


@app.route('/display/<expr>')
def display(expr):
  return "equation %s" % (expr) 


@app.route('/' , methods=('GET' , 'POST'))
def home():
  if request.method == "POST":
    expr = request.form['equation']
    return redirect(url_for('display' , expr = expr))
  
  return render_template("index.html")


if __name__ == "__main__":
  app.run(debug=True)
