---

layout: ots
title: Files & Templates

---

## Files

So you've seen how to send out some basic text with a simple Flask application, and the languages that are used to build the web: HTML, CSS and Javascript. Serving text isn't enough though - what if we want to serve some actual files?

Luckily, Flask comes prepared. All you have to do is **create a folder** in the same directory as `catseverywhere.py` with the special name of `static`. Any file you put in that folder will be served by Flask automatically! It's one of the nice functionalities provided to you by Flask's authors.

You can do this with your computer's file browser, or on the command line by typing `mkdir static`.

So, if you made a file in the static folder called `cats.gif`, and you'd normally access your application by visiting the url [http://127.0.0.1:5000](http://127.0.0.1:5000), then you can view that file by going to [http://127.0.0.1:5000/static/cats.gif](http://127.0.0.1:5000/static/cats.gif).

**Check this works** for you by downloading a funny image from the internet (there are plenty at [imgur](http://imgur.com)), putting it in the static folder, running your Flask application (`python catseverywhere.py`), and browsing to your image by the right url.

The `static` folder is a great place to put CSS stylesheets, Javascript script files, and images. Those files don't usually change much when a website is running, hence the folder name. A common practice is that web developers will organise these files in sub-directories called, for instance, `css`, `js`, and `img` respectively. 

## HTML Templates

None of that explains where to put the *content* of our application - the HTML. Flask makes use of HTML templating - this allows it to put dynamic application data (like a list of email addresses that changes over time) into HTML easily, so that any web browser can view it easily, and it looks good as well.

Flask uses another special directory to store templates, called `templates` (crazy, huh?), **so go ahead and create it**, like you did for `static`.

In it, **create a file** called `index.html` inside of `templates` directory and chuck some in some HTML -

{% raw %}

    <!DOCTYPE html>
    <html>
      <head>
        <title>{{ author }}'s app</title>
      </head>

      <body>
        <h2>Hello {{ name }}!</h2>
      </body>
    </html>

{% endraw %}

This is a pretty simple HTML page, but it includes two simple bits of Flask's templating language. When Flask shows this template to your browser, it will replace {% raw %}`{{ author }}` and `{{ name }}`{% endraw %} with what you assign those two variables in your application. If author was assigned to be "Bob", then the title of the page served will be "Bob's app".

In this way a template separates what the content of the page should be, from the actual actual _data_ that will be used as that content. This makes things a whole lot easier if you have to write a lot of dynamic web pages!

Flask's templates can do a good deal more than just display variables, but we can get to that in good time.

Let's **modify our flask app** to serve this template:

    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        author = "Me"
        name = "You"
        return render_template('index.html', author=author, name=name)

    if __name__ == "__main__":
        app.run()

You can see we imported a new function from `flask`, called `render_template`.

Then in `hello_world()`, we added two variables called `author` and `name`. **Please change their values** from `"Me"` and `"You"` in your file, those are boring!

Then instead of returning some text, we returned the result of calling `render_template`. First, we give it the file name of the template we wish to process. Then, we pass in the variable names that the template should know about (`author` and `name`) and what their values should be (...coincidentally, `author` and `name`!). This function should load up the template, do the processing required to replace placeholders with values, and return the full HTML text.

Now try running and viewing your app, in all its HTML glory!

## A prettier home page

Now that we have a bit more confidence in changing the home page we can look at making something a bit prettier. We want the home page of _Cats Everywhere_ to be fun and exciting. Something that says "Yes, these people know what they are doing. I will give them my email address in hope of seeing more of their work in future."

This means fancy fonts, large bold type, huge banner images and nice round corners and things. We are going to need some more interesting HTML and a fair bit of CSS to get it looking pretty.

We've prepared a self-contained template that you can use for the home page. You can download it [here](https://raw.github.com/OpenTechSchool/python-flask-code/master/core/files-templates/templates/index.html) and save it as `index.html` in your templates directory.

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Cats Everywhere!</title>	

        <link     href='http://fonts.googleapis.com/css?family=Sintony:400,700'     rel='stylesheet' type='text/css'>

        <style type="text/css">    
          body
          {
            background-color:#000;
          }

          h1
          {
            font-size:48px;
            margin-top:0;
            font-family:Arial, sans-serif;
            text-shadow:2px 0 15px #292929;
            letter-spacing:4px;
            text-decoration:none;
            color:#DDD;
          }

          #banner
          {
            width:500px;
            height:200px;
            text-align:center;
            background-image:url(http://i.imgur.com/MQHYB.jpg);
            background-repeat:no-repeat;
            border-radius:5px;
            margin:90px auto auto;
            padding:80px 0;
          }

          .lead
          {
            background-color:rgba(255,255,255,0.6);
            border-radius:3px;
            box-shadow:rgba(0,0,0,0.2) 0 1px 3px;
            font-family:Sintony, sans-serif;
          }
        </style>

      </head>  

      <body>
        <div id="banner">
          <h1>cats everywhere</h1>
          <p class="lead">We're bringing cats to the internet. Free.     Cute. Awesome.</p>
        </div>
        <div id="emailform">

        </div>
      </body>
    </html>

It should look a little something like this:

![](https://pbs.twimg.com/media/BGPsFh9CYAAcrct.png:large)
