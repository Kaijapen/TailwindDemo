from flask_app import app
from flask import render_template, redirect, request, flash, session
# import your models as needed


@app.route('/')
def start():
    return render_template("index.html")
