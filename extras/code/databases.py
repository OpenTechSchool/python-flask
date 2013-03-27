from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import g
import sqlite3

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/signup.html', methods = ['POST'])
def signup():
    email = request.form['email']
    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')

@app.route('/emails.html')
def emails():
    email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
    return render_template('emails.html', email_addresses = email_addresses)

if __name__ == '__main__':
	app.run(debug=True)
