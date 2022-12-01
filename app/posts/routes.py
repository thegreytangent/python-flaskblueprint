from  app.posts import bp
from flask import render_template

@bp.route("/")
def index() : 
    return render_template('posts/index.html')

@bp.route("/categories/")
def categories():
    return render_template('posts/categories.html')