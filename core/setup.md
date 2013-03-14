---

layout: ots
title: Setup

---

# Python 2 or Python 3?

There is currently a split in the Python community between Python 2 and Python 3. Though Python 3 has been around for some time now, there are still many programs which run on Python 2. It is very common in programming to have this sort of version split over time, as many programs can't keep up with the pace of change as a language evolves.

For this workshop it is recommended to use Python 2.7, but we will try to keep things compatible with Python 3 users as well.

Flask recommends Python 2.7, which might be different from the version that you have installed right now. You can see what version of Python is installed by starting the Python interpreter. For example on Linux and OSX you can run the `python` command:

    $ python
    Python 2.7.3 (default, Sep 26 2012, 21:53:58) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Here you can see it is version `2.7.3`. If you don't have Python installed or you have Python 2 then continue reading. If you have Python 3 and want to keep using it then skip over the Python 2.7 installation and go straight to `pip`.

# Python 2.7

If you don't have 2.7 installed then you can download and install it here:

* [Windows 32-bit](http://www.python.org/ftp/python/2.7/python-2.7.msi) and [Windows 64-bit](http://www.python.org/ftp/python/2.7/python-2.7.amd64.msi).
* [Mac OSX](http://www.python.org/ftp/python/2.7/python-2.7-macosx10.5.dmg)
* With Linux, most distributions will already have Python 2 installed.

# pip

The `pip` command uses the [Python Packages Index](https://pypi.python.org/pypi) to install new Python libraries. This makes it super-easy to install Flask and other libraries that you might want to use in future, like for example [Twitter](https://pypi.python.org/pypi/twitter/1.9.1) or  [bashplotlib](https://pypi.python.org/pypi/bashplotlib/0.4.4).

## Windows

To install pip on Windows, download and run [distribute_setup.py](http://python-distribute.org/distribute_setup.py). This will install the `easy_install` command into the `Scripts` folder under your Python installation. For example, into `C:\Python27\Scripts\easy_install` if you used the default install.

With `easy_install` you can use that to install `pip` using the command prompt:

	$ C:\Python27\Scripts\easy_install pip

Now you will have `pip` installed in the Scripts folder as well.

## Mac OSX

The `pip` command might already be installed, try running `pip` in the command prompt. If that didn't work then try:

	sudo easy_install pip

## Linux

Many Linux distributions include a package for pip. For example on Ubuntu you can install it with:

	sudo apt-get install python-pip

# virtualenv

This part isn't required for Flask, but many people find it very useful to be able to separate their projects in terms of library installations and Python versions. You can skip over this section if you like, or come back to it later.

Virtualenv makes it easy to use Python 2.7 in one project and Python 3 in another. It also gives you a place to install libraries _per-project_, so you can have one project using Flask, another using Django, another using Bottle and their won't step all over each other.

Installing on Windows is as easy as:

	c:\Python27\Scripts\pip install virtualenv

On OSX, try

	sudo pip install virtualenv

To install on Linux you can often find virtualenv already packaged for you. For example on Ubuntu you can do:

	sudo apt-get install python-virtualenv
	
Now that it is installed, we can set up virtualenv for this workshop. This will keep Flask and it's dependencies contained to just this workshop:

On OSX and Linux:

	# Create the directory for this workshop
	mkdir flask-workshop
	cd flask-workshop
	# Create a Python 2.7 virtualenv under the 'venv' directory
	virtualenv --python=python2.7 venv
	# Activate the virtual environment
	source venv/bin/activate
	
On Windows:

	# Create the directory for this workshop
	mkdir flask-workshop
	dir flask-workshop
	# Create a Python 2.7 virtualenv under the 'venv' directory
	C:\Python27\Scripts\virtualenv venv
	# Activate the virtual environment
	venv\Scripts\activate

The last step, _activate_ sets your terminal/command prompt session for using the Python installation in the `flask-workshop` directory. If you start up a new terminal then you will need to repeat the activation step again.

The `deactivate` command can be used to return your terminal back to normal. But for now let's leave it activated because it's time to install Flask.

# Installing Flask

So far as website frameworks go, Flask has a minimal number of libraries that it needs to run. Though it would be possible to find and install all these libraries manually it is much easier to use the `pip` command.

## On Python 2.7

Now that everything is set up, installing Flask is as easy as:

	pip install flask

## On Python 3

Though the official Flask doesn't run on Python 3, someone has kindly done the work to port it and published the result.

With `pip`, you can install Flask with this:

	pip install https://github.com/puzzlet/itsdangerous/tarball/py3 https://github.com/puzzlet/werkzeug/tarball/py3-dev https://github.com/puzzlet/flask/tarball/py3

If you don't feel like installing them all at once you can do it one-by-one:

	pip install https://github.com/puzzlet/itsdangerous/tarball/py3
	pip install https://github.com/puzzlet/werkzeug/tarball/py3-dev
	pip install https://github.com/puzzlet/flask/tarball/py3

Then you are good to go with Flask on Python 3.