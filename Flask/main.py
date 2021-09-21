from flask import flask,render_template
import random

from flask import Flask

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/2")
def pag2():
    return render_template("segunda.html")

@app.route("/3")
def pag3():
    return render_template("tercera.html")

if __name__=='__main__':
    app.run(host='0.0.0.0',port=random.randint(2000,9000))