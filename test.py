from flask import Flask,redirect,render_template,session,url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hoidepzai'
@app.route('/')
def index_page():
    return render_template('index.html')
