from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    text = 'ovo je početna stranica!'
    return render_template('index.html',text=text)

@app.route('/links')
def links():
    links = {'Strukovna škola Vice Vlatkovića': 'https://ssvv.hr/',
             'PMF Split': 'https://www.pmfst.unist.hr/',
             'Thousands of free icons': 'https://icon-icons.com/',
             'Flask-Bootstrap': 'https://pythonhosted.org/Flask-Bootstrap/index.html'
             }
    return render_template('links.jinja',links=links)

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
