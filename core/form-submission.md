---
layout: ots
title: Form Submission
---

Rumours of _Cats Everywhere_ have sent the web into a frenzy. Now is the time to move our dusty old static landing page into an exciting and invigorating sign-up page!

To do this we will need two things:
* A HTML form on the web page. This will have a text input field and a submit button.
* A _route_ in our Flask app to accept the data posted by the form.

At the moment we will just print out the email addresses that we receive directly to the console.

# HTML Form

The form is simple enough:

	<form action="signup.html" method="post">
		<input type="text" name="email"></input>
		<input type="submit" value="Signup"></input>
	</form>

Place this form inside the `<body>` section of the landing page. You can fiddle around a bit to get it in the place you want.

# Python route

Now the action attribute of the form is saying it will be posted to `signup.html`. We don't have any code for this URL at the moment, so it is time to make some!

We are going to need to import more objects from Flask. We need `request` to get the form data, `redirect` to redirect the browser once we are done.

	from flask import request, redirect

Now we can add our new route for `signup.html`.

	@app.route('/signup.html', methods = ['POST'])
	def signup():
	    email = request.form['email']
	    print("The email address is '" + email + "'")
	    return redirect('/'))

This gets a little complicated, so we'll go through it line-by-line:

	@app.route('/signup.html', methods = ['POST'])

We apply a _decorator_ to the signup function, saying that we want it to be used when the browser requests `/signup.html`. It will accept the HTTP _POST_ method, which you can see is mentioned in the HTML form element as `method="post"`.

	def signup():
	    email = request.form['email']
	    print("The email address is '" + email + "'")

In the signup method we can retrieve the email address using the `request` object, which contains the form data. In the HTML we used `name="email"`, which means that in the `request` object we can use `request.form["email"]`. If we used `name="address"` in the HTML then it would be `request.form["address"]`.

When we write `request.form["email"]` we are using `request.form` as a Python Dictionary, looking up the entry held in there for `"email"`. Dictionaries are a type of data structure we haven't seen before, we'll talk about them more in the Data Structures chapter.

At this stage We just print out the email address that's supplied. So when you submit the form you should be able to see the address you supplied printed out on the console.

	    return redirect('/')

Once we have printed the email address we still need a response to send back to the web browser. A common option is to send a HTTP _Redirect_ response. This tells the browser to go to another page. In our case we just send them back to the home page, `/`, which is served by the `hello_world()` function.