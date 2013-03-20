from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

email_addresses = []

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/signup.html', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses = email_addresses)

if __name__ == '__main__':
	app.run()
