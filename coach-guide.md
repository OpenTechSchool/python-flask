---

layout: ots
title: Coach Guide

---

Thanks for coaching! Check out the generic [OpenTechSchool coaching guide](http://opentechschool.github.com/slides/presentations/coaching/) as well!

## Python

We are recommending Python 2.7 for this workshop, though they can use Python 3 if they use the custom version of Flask in the setup section.

With Python installed, we then recommend using [distribute](http://pythonhosted.org/distribute/)'s `easy_install` to install [pip](https://pypi.python.org/pypi/pip), then using pip to install [virtualenv](https://pypi.python.org/pypi/virtualenv).

Then with virtualenv they can create an isolated installation of Python inside their working directory for the workshop. Once they have run the virtualenv activate script then when they run `pip install flask` it will install Flask to their working directory instead of the system Python.

## Flask

This workshop is concerned with building a simple website with Python Flask. There are two parts:

* A home page containing a form for submitting an email address.
* A page for listing the submitted emails.

A Flask app is just a single Python file with a function for each URL in the web app. It has a simple template system and we just use an in-memory list to store the email addresses.

See it running on Heroku: Here is the [home page](http://python-flask-code.herokuapp.com/) where people can enter their email address and the [emails page](http://python-flask-code.herokuapp.com/emails.html) where you can view the list of submitted emails.

You can see the source code for the final example [here](https://github.com/OpenTechSchool/python-flask-code/tree/master/core/data).

Finally, the [Flask Documentation](http://flask.pocoo.org/docs/) is quite comprehensive and covers a lot of topics about building a website. The reason we chose Flask (over Bottle et al) is that the documentation is very good. So we encourage you to send people there!

## HTML/CSS/Javascript

Participants will likely have questions about HTML and CSS. We have some links in the extras section for learning more which you can direct them to. There is also the 'Professional CSS' section if they are interested in hardcore stuff like Twitter Bootstrap, SASS and LESS.

For this workshop the focus is on what the website can _do_, not what the website looks like. So perhaps try to ask people what things they want their sites to do rather than how they look.

## Help with Windows

Windows can be a little annoying to set up. Because people will probably end up with multiple installations of Python I wouldn't recommend setting up PATH. Instead, just use the full path to `python.exe` and scripts. It only needs to be done to get virtualenv. Once they have activated a virtualenv environment then they will not need to use full paths.