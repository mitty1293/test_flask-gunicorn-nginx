import random, string
from flask import render_template, redirect, url_for, flash
from app import app

app.secret_key = "".join([random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&') for i in range(12)])

@app.route('/')
def index():
    app.logger.info("info: accessed /")
    app.logger.debug("debug: accessed /")
    app.logger.warn("warn: accessed /")
    return render_template("index.html")

@app.route('/string_test/<string:some_string>')
def string_test(some_string):
    return render_template("string_test.html", some_string=some_string)

@app.route('/redirect_test')
def redirect_test():
    # flash("リダイレクトされました")
    # return redirect(url_for('redirect_result'))
    # return redirect('/redirect_result')

    resp = redirect(url_for('redirect_result'))
    resp_headers_str = str(resp.headers)
    with open("/var/log/flask_header.log", mode="w") as f:
        f.write(resp_headers_str)
    return resp

@app.route('/redirect_result')
def redirect_result():
    return render_template("redirect_result.html")
