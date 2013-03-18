---
layout: ots
title: Form Submission
---

Rumours of _Cats Everywhere_ have sent the web into a frenzy. Now is the time to move our dusty old static landing page into an exciting and invigorating sign-up page!

To do this we will need two things:
* A HTML form on the web page. This will have a text input field and a submit button.
* A _route_ in our Flask app to accept the data posted by the form.

At the moment we will just print out the email addresses that we receive.

# HTML Form

The form is simple enough:

	<form action="signup.html" method="post">
		<input type="text" name="email"></input>
		<input type="submit" value="Signup"></input>
	</form>

Place this form inside the `<body>` section of the landing page. You can fiddle around a bit to get it in the place you want.

# Python route

Now the action attribute of the form is saying it will be posted to `signup.html`. We don't have any code for this URL at the moment, so it is time to make one!

We are going to need to import more objects from Flask. We need `request` to get the form data, `redirect` to redirect the browser once we are done and `url_for` to generate the URL back to the main page.

	from flask import request, redirect, url_for




