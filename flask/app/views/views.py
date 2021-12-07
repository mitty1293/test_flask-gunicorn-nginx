import random, string
from flask import render_template, redirect, url_for, flash
from app import app

app.secret_key = "".join([random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&') for i in range(12)])

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/redirect_test')
def redirect_test():
    # flash("リダイレクトされました")
    return redirect(url_for('redirect_result', _external=True))
    # return redirect('/redirect_result')

@app.route('/redirect_result')
def redirect_result():
    return render_template("redirect_result.html")
