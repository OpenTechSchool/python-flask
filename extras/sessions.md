---
layout: ots
title: Keeping track of users
---

## What are sessions, and why do we need them?

HTTP is, by itself, a _stateless_ protocol. That means it doesn't keep track of information or change much in-between requests. You should see the conundrum implicated by this if you look at the fact that practically every application on the web _does_ keep track of information - namely, they mostly keep track of you. If facebook was purely stateless, it wouldn't be able to recognise that you were logged in from one page to another - and probably wouldn't be very popular!

A session then, is simply the name web developers usually give to the mechanism that lets you do this when serving (running) a web application.

If you'd like to know how it works, the web server is usually instructed to send your browser a [HTTP cookie](http://en.wikipedia.org/wiki/HTTP_cookie_) along with the page content, when you visit. The cookie holds a unique value - that your browser will send back to the server with every request - that the application can then look up and re-identify  you with when you ask for another page.

In case you were wondering, when we run flask, it is acting as both a web server _and_ the web application (nicely bundled together to be easy to use!).

## So flask has sessions, right? How does one use them?

It sure does, and they're very simple to use. Firstly, **add `session` as another module to import** from the `flask` package:

    from flask import session
    
Then you need to give flask a secret key to use, to make sure the session is secure. To get a nice secret key, **run this at a command prompt**:

     python -c "import os; print repr(os.urandom(24))"
     
and copy the string you get. To set this as the flask app's secret key, just **add the following line** after you initialize your `app` (use your own key!):

    app.secret_key = '#d\xe9X\x00\xbe~Uq\xebX\xae\x81\x1fs\t\xb4\x99\xa3\x87\xe6.\xd1_'
    
You can now use the `session` that you imported, just as you would a dictionary - anywhere in your application. It will be a special dictionary, in that any key/value you set will be specific only for the user you set it to. When a different user visits your server, it will hold their own value (or not be there).

How can we use this? Let's say we would like users to be able to delete their own email off of the email list.

First, we have to **modify the `signup()` route** to remember the user's email address in the session:

    @app.route('/signup.html', methods = ['POST'])
    def signup():
        email = request.form['email']
        email_addresses.append(email)
        session['email'] = email
        print(email_addresses)
        return redirect('/')
        
You can see that we simply added a line to save that email to our session dictionary.
        
Then we can **create a new route**, that the user can visit to delete their address.

    @app.route('/unregister')
    def unregister():
        # Make sure they've already registered an email address
        if 'email' not in session:
            return "You haven't submitted an email!"
        email = session['email']
        # Make sure it was already in our address list
        if email not in email_addresses:
            return "That address isn't on our list"
        email_addresses.remove(email)
        del session['email'] # Make sure to remove it from the session
        return 'We have removed ' + email + ' from the list!'


Here, we use a few `if` checks to make sure that our user added an email address already, and it's in our list. We can't remove it otherwise! Read through the code and the comments careful to make sure you understand what's happening.

**Try out the new functionality!** Add an email address, and then visit `/unregister` in your web browser. When you next look at the list, your email address should have been removed!

### Extensions
