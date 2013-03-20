---

layout: ots
title: Data Structures in Python

---

# Understanding data structures

Back in the first session we introduced three of the most common data types used in programming: numbers, strings and booleans. We assigned those data types to variables one-by-one, like so:

	  x = 3          # numbers
	  a = "gorillas" # strings
	  t = True       # booleans

But what if we need something more complicated, like a shopping list? Assigning a variable for every item in the list would makes things very complicated:

	  item_1 = "milk"
	  item_2 = "cheese"
	  item_3 = "bread"

## Lists

Fortunately we don't have to do this. Instead, we have the ``list`` data type. An empty list is simply ``[]``

	  shopping_list = []

When you are in the Python interpreter you can see what is inside a list by just typing the name of the list. For example:

	  >>> shopping_list
	  []

The interpreter shows us that the list is empty.

Now we can add items to ``shopping_list``. Try typing the following commands into the Python interpreter.

	  shopping_list.append("milk")
	  shopping_list.append("cheese")
	  shopping_list.append("bread")

What is in the shopping list? What happens when you append numbers or        booleans to the list?

To remove an item from the list we use ``remove()``:

	  shopping_list.remove("milk")
      
Lists can easily be processed in a ``for`` loop. Have a look at this example which prints each item of the list in a new row:

    for item in shopping_list:
		print(item)

And that's it! Lists are the most common data structure in programming. There are lots of other things you can do with lists, and all languages have their own subtly different interpretation. But fundamentally they are all very similar.

In summary:

	  shopping_list = []
	  shopping_list.append("cookies")
	  shopping_list.remove("cookies")

## Dictionaries

The other main data type is the dictionary. The dictionary allows you to associate one piece of data with another. The analogy comes from real-life dictionaries, where we associate a word with it's meaning. It's a little harder to understand than a list, but Python makes them very easy to deal with.

You can create a dictionary with ``{}``

	  foods = {}

And you can add items to the dictionary like this:

	  foods["banana"] = "A delicious and tasty treat!"
	  foods["dirt"]   = "Not delicious. Not tasty. DO NOT EAT!"

As with lists, you can always see what is inside a dictionary:

	  >>> foods
	  {'banana': 'A delicious and tasty treat!', 'dirt': 'Not delicious. Not tasty. DO NOT EAT!'}

And you can also delete from a dictionary as well. We don't really need to include an entry for dirt:

	  del foods["dirt"]

What makes dictionaries so useful is that we can give meaning to the items within them. A list is just a bag of things, but a dictionary is a specific mapping of something to something else. By combining lists and dictionaries you can describe basically any data structure used in computing.

For example, you can easily add a list to a dictionary:

	  ingredients = {}
	  ingredients["blt sandwich"] = ["bread", "lettuce", "tomato", "bacon"]

Or add dictionaries to lists:

	  europe = []
	  germany = {"name": "Germany", "population": 81000000}
	  europe.append(germany)
	  luxembourg = {"name": "Luxembourg", "population": 512000}
	  europe.append(luxembourg)

Outside of Python, dictionaries are often called ``hash tables``, ``hash maps`` or just ``maps``.

# Storing email addresses

At the moment we don't have any way to store email addresses. But if we add a list to our website then we can keep them temporarily. Sure it will only stay around until the web server stops, but it is a good start.

Let's add a list to the top of the Python code, just after all the `import` lines and `app = Flask(__name__)`:

	email_addresses = []

Now in our `signup()` function we can add the email address instead of printing it.

	@app.route('/signup.html', methods = ['POST'])
	def signup():
	    email = request.form['email']
	    email_addresses.append(email)
	    print(email_addresses)
	    return redirect('/')

# Listing email addresses

Printing out our email addresses to the console is a bit of a hassle. If you wanted to read the list then you have to open the terminal and scan through for the printout. It would be so much easier to have a web page that lists all the email addresses that we have collected.

We know how to create a new page in Flask, it's just a function. And we can pass the list of emails directly to our HTML template like so:

	@app.route('/emails.html')
	def emails():
	    return render_template('emails.html', email_addresses = email_addresses)

Here the `render_template()` function takes the name of the template (`'emails.html'`) and extra data to be used when rendering the page. We wrote `email_addresses = email_addresses` to say that our variable `email_addresses` will be available in the template using the same name.

Now we need our HTML template. In our previous template we didn't actually do anything but plain HTML. But now we need to print the list of email addresses, so we'll use a `for` loop in the template.

Here is the content of `email.html` for the _templates_ directory:

{% raw %}

	<html>
	  <head>
	    <title>Cats Everywhere email addresses</title>
	  </head>
	  <body>
	    <p>Here are all the emails we have collected:</p>
	    <ul>
	      {% for email in email_addresses %}
	      <li>{{ email }}</li>
	      {% endfor %}
	    </ul>
	    <p>THIS IS GONNA ROCK!</p>
	  </body>
	</html>

{% endraw %}

