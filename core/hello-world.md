---

layout: ots
title: Hello World

---

Now that we have Python and Flask installed it's time to start with our first website. But first we need to know a little about how the web browser retrieves data from a web server.

# HTTP

The HyperText Transfer Protocol is the network communication between your web browser and the server. In HTTP, the browser makes a _request_ and the server sends back a _response_.

There are two main types of request, `GET` and `POST`.

* The browser sends a `GET` request to retrieve data. For example, going to `http://www.opentechschool.org/team.html` will cause the browser to send `GET /team.html` to the server.
* The `POST` request is used to send data. For example if you fill out a web form and click `Submit` it will send the form data back to the server.

We will be doing both GET and POST requests today. First we'll handle a GET request with the Hello World example. Then in a later chapter we will try POST.

# Hello World - A Static Website

In the early days people would write HTML files in a directory being watched by an Apache server. It was simple, but limiting. The content was _static_, with no way to make it change without editing the files on the server. Today we are going to start with something just as simple. This is the [Quickstart example](http://flask.pocoo.org/docs/quickstart/) from the Flask documentation.

Open a new file called `hello.py` in your workshop directory. This might look a little cryptic:

	from flask import Flask
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
		return 'Hello World!'

	if __name__ == '__main__':
		app.run()


Let's break it down a little:

	from flask import Flask
	app = Flask(__name__)

This imports the Flask library and creates a new website in a variable called `app`.

	@app.route('/')
	def hello_world():
		return 'Hello World!'

The `@` is new, it's called a _decorator_ and it is used to give meaning to function definitions. In this case it says that if the browser requests the address `/`, then the website should _route_ that request to the `hello_world` function.

The function itself returns the string "Hello World!". This will be sent to the web browser.

	if __name__ == '__main__':
		app.run()

This is Python for  "if this script is run directly then start the application".

Now you can start running your first website!

	$ python hello.py 
	 * Running on http://127.0.0.1:5000/

Open that address in your browser! It probably looks something like this:

![](images/hello-world.png)

Hmmm, looks a little basic. In the next section we will look at making it a little better looking.