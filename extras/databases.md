---
layout: ots
title: Databases
---

There is a reason why we haven't used a more permanent method for storing our email addresses, and that's because _databases are complicated_. Seriously.

But fortunately they are not that difficult once you get the hang of it. Since the 1970s many databases have standardised on using the **SQL** language. It defines how to store and search data in _tables_, which contain _columns_, and rows of data usually referred to as _records_. If you learn SQL then you can use quite a lot of different databases.

Because of their size and complexity databases are generally written as their own separate servers that run in addition to your web server. That comes with additional work that we probably don't need at this moment. For now we'll use [SQLite](http://www.sqlite.org/) which is a simple and very widely used database engine that just happens to come bundled in Python.

## Creating the database

Since Python 2.5 the SQLite library has shipped in the standard distribution. This means it should be available already. You can import the `sqlite3` library in a Python shell to see if it works:

    >>> import sqlite3

We are going to start by creating a database in a file called `emails.db`. It will have one table called `email_addresses` which will keep all our emails. Make sure your Python shell started in the same directory as your website code.

    >>> conn = sqlite3.connect("emails.db")
    >>> cursor = conn.cursor()
    >>> cursor.execute("CREATE TABLE email_addresses ( email TEXT );")
    <sqlite3.Cursor object at 0xb7467ce0>

Here you can see we connected to `emails.db` (this file didn't exist, so SQLite created it). We opened a _cursor_, which is what allows us to send commands, and executed a _CREATE TABLE_ statement to create the email addresses table. It has one column, _email_, which can just be a string of text.

## Using SQLite in Flask

The Flask documentation has a [section](http://flask.pocoo.org/docs/patterns/sqlite3/) on using SQLite which we will use here. It recommends that we store the database connection in a global variable, and open/close the connection before and after every request.

We'll need to import the `g` object from Flask, as well as `sqlite3`:

    from flask import g
    import sqlite3

Now we use `@app.before_request` to run a function before every request from the browser:

    @app.before_request
    def before_request():
        g.db = sqlite3.connect("emails.db")

Likewise we use `@app.teardown_request` to close the database connection after every request.

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'):
        g.db.close()

## Adding a new email address

Now that we have everything installed and set up we can just use an SQL _INSERT_ statement to add new email addresses to the table.

    @app.route('/signup.html', methods = ['POST'])
    def signup():
        email = request.form['email']
        g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
        g.db.commit()
        return redirect('/')

Notice that we use `g.db.commit()`. If you don't use `commit()` then it won't save the email address!

## Listing email addresses

Now that we have all our emails stored in a database we have to use a _SELECT_ statement to get them all back. Let's update the `emails()` function to use the database:

    @app.route('/emails.html')
    def emails():
        email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
        return render_template('emails.html', email_addresses=email_addresses)

You might notice that the list of emails now looks a little strange on the web page. This is because the `g.db.execute()` statement returns an entire tuple for _every_ email address. In the Python console it looks like this:

    >>> db.execute('select * from email_addresses').fetchall()
    [(u'eroaskdlg',), (u'kjzdfhks',), (u'lksrlajkr',)]

So every item in the list is actually a tuple (a non-modifiable list). The email itself is at position 0 in each tuple. So update the emails template to print just the first element:

{% raw %}

    <ul>
      {% for email in email_addresses %}
      <li>{{ email[0] }}</li>
      {% endfor %}
    </ul>

{% endraw %}

And that's it! You can now restart the web server as many times as you like, and your list of emails will remain! All the emails are now stored directly in the database.

## Further Reading

* [Learn SQL the Hard Way](http://sql.learncodethehardway.org/) is currently in alpha, but many have enjoyed other books in the series.
* [Python sqlite documentation](http://docs.python.org/2/library/sqlite3.html) describes the Python API for SQLite.
* SQLite has [SQL Syntax](http://www.sqlite.org/lang.html) and [Data types](http://www.sqlite.org/datatype3.html) references.
