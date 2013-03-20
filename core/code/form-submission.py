from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/signup.html', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)
