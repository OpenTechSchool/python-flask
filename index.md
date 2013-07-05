---

layout: ots
title: Websites with Python Flask

---

This is the course content for Websites with Python Flask, which has been developed and maintained by [OpenTechSchool](http://www.opentechschool.org).

# Welcome

Hi, welcome to Websites with Python Flask. In this workshop we will take you through the fundamentals of creating dynamic websites using the Python Flask library. After the workshop you should have a rough mental picture of how websites work and some good pointers for getting further with websites of your own.

We only expect you to know a little Python, like from our [Introduction to Programming](http://opentechschool.github.com/python-beginners/en/index.html) workshop. You definitely do not need to know a lot. It will be best if you have a recent version of Python installed as well (version 2.7 or 3.3+).

Don't worry if you know only a little HTML or none at all. We'll be looking at how it all works rather than how to make it look pretty. HTML is important, but it's only one part of making a website.

## What we'll do today

So we have this awesome idea for a website, _Cats Everywhere_, which lets people share pictures of cats *via the internet*. It's innovative, it's new, it's exciting...

But we don't have any code yet.

Instead we'll make a _landing page_, letting the internet know that a new era of cat pictures will soon begin. People can submit their email address to learn more when the real site goes live. By storing those addresses we'll have a ready-made audience when the time comes to announce the real thing.

We'll be using Python Flask as the web server. Cat lovers will be able to point their web browsers at our site, enter their email address, and hold their breath for the exciting launch!

We've put the final product online so you can see what we are aiming to do today. Here is the [home page](http://python-flask-code.herokuapp.com/) where people can enter their email address and the [emails page](http://python-flask-code.herokuapp.com/emails.html) where you can view the list of submitted emails.

## A bit of history

Websites as we know them today started in 1991 from the work of Tim Berners-Lee at CERN. Most websites were static content; simple HTML pages stored on disk and sent directly to the browser. If people wanted to interact with others then they would have to do it by other means, such as email or USENET.

Web servers eventually enabled programmers to write dynamic interactive websites in a variety of languages such as Perl and Python. This interface was called CGI (Common Gateway Interface) and is still found in some places, though it is generally considered too awkward for everyday use now.

Since 1996 the most common web server has been Apache HTTPD, but from the late 1990s it was possible to build dynamic websites using a number of other language-specific platforms. Popular choices were Servlets (Java), Perl, PHP, Zope (Python) and ASP (Microsoft IIS).

When the web became ubiquitous in the early 2000s many programmers were fed up with the work required to build and maintain large websites. From previous experience new platforms were built. Of these the most popular by far are Ruby on Rails and Python Django. These very large frameworks controlled the vast majority of the developer experience. Once set up they can make complicated websites very quickly, but also require a lot of experience to master.

Many developers did not require such large and complicated tools and so now we also have the _microframeworks_. As well as Flask, which we'll be using today, there are other popular microframeworks. These include:

* Sinatra (which uses the programming language Ruby).
* Express (which uses the programming language JavaScript).
* Bottle (which uses Python).

These are all small focused libraries that provide just the bare essentials, but can usually be extended into more complicated solutions.

# Core workshop material

* [Setting up](core/setup.html) - Installation instructions for Windows, OSX and Linux.
* [Hello, World!](core/hello-world.html) - Serving our first web page.
* [HTML, CSS and JavaScript](core/html-css-js.html) - A quick tour of fundamental web technologies.
* [Files & Templates](core/files-templates.html) - How to show pictures of cats, and a prettier version of our home page.
* [Forms](core/forms.html) - How forms work on the web.
* [Form Submission](core/form-submission.html) - Receiving and processing the form.
* [Data Structures](core/data.html) - Storing our emails and displaying dynamic lists in web pages.

Want to compare your code? You can browse the code examples directly on GitHub [here](https://github.com/OpenTechSchool/python-flask-code). We've organised it by section. You can see the source code for the final example [here](https://github.com/OpenTechSchool/python-flask-code/tree/master/core/data).

# Extra fun stuff

Of course the core workshop can't cover everything. But we've prepared these extra topics to guide you with things you might be interested in. You can pick-and-choose whichever ones you want, they are all independent of each other.

* [Learning HTML and CSS](extras/learn-html-css.html) - More on creating web pages.
* [Professional CSS](extras/css.html) - How the pros style their websites.
* [Keeping track of users](extras/sessions.html) - Using sessions to persist data over multiple visits.
* [Using Databases](extras/databases.html) - How to store data permanently.
* [Hosting on Heroku](extras/heroku.html) - Host your website for free online using Heroku.

# Reference material

* [Python Lists API](http://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) and  [Python Dictionaries API](http://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
* [Flask Documentation](http://flask.pocoo.org/docs/) - Quickstart, User Guide and Reference.
* [Jinja Documentation](http://jinja.pocoo.org/docs/templates/) - For the HTML templates used in Flask.
* [Popular Web Frameworks](reference/web-frameworks.html) - Some of the more popular website platforms at the moment.

