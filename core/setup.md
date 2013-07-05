---

layout: ots
title: Setup

---

# Installing Python

This workshop uses Python If you don't have it installed then you can download and install it here:

* [Download Python](http://www.python.org/getit/)

At the moment both 2.7 and 3.3 are supported.

# pip

Python comes with a lot of built-in functionality in the form of modules. For example, we used the `turtle` module in the Introduction to Programming course. However, Python doesn't come with everything you might need. You can extend Python by adding new modules, which come bundled up in _packages_.

The `pip` command uses the [Python Packages Index](https://pypi.python.org/pypi) to install new Python packages. This makes it super-easy to install Flask and other packages that you might want to use in future, for example [Twitter](https://pypi.python.org/pypi/twitter/1.9.1) (to access the Twitter API to request data about Twitter) or [bashplotlib](https://pypi.python.org/pypi/bashplotlib/0.4.4) (to plot data on a graph in your terminal.)

## Windows

To install pip on Windows, download and run [distribute_setup.py](http://python-distribute.org/distribute_setup.py). This will install the `easy_install` command into the `Scripts` folder under your Python installation. For example, into `C:\Python27\Scripts\easy_install` if you used the default install.

With `easy_install` you can use that to install `pip` using the command prompt:

    $ C:\Python27\Scripts\easy_install pip

Now you will have `pip` installed in the Scripts folder as well. If you like, you can ask us about adding the Python and scripts directories to the windows PATH; this will let you type `python` or `pip` at your command prompt directly.

## Mac OSX

The `pip` command might already be installed, try running `pip` in the command prompt. If that didn't work then try:

    sudo easy_install pip==1.2.1

On Mac OSX we use an older version of `pip` to workaround errors in the Mac OSX installation of OpenSSL. Details [here](https://github.com/pypa/pip/issues/829).

## Linux

Many Linux distributions include a package for pip. For example on Ubuntu you can install it with:

    sudo apt-get install python-pip

# virtualenv

This part isn't required for Flask, but many people find it very useful to be able to separate their projects in terms of package installations and Python versions. You can skip over this section if you like, or come back to it later.

Virtualenv makes it easy to use Python 2.7 in one project and Python 3 in another. It also gives you a place to install libraries _per-project_, so you can have one project using Flask, another using Django, another using Bottle and they won't step all over each other.

Installing on Windows is as easy as:

    c:\Python33\Scripts\pip install virtualenv

On OSX, try

    sudo pip install virtualenv

To install on Linux you can often find virtualenv already packaged for you. For example on Ubuntu you can do:

    sudo apt-get install python-virtualenv
	
Now that it is installed, we can set up virtualenv for this workshop. This will keep Flask and it's dependencies contained to just this workshop:

On OSX and Linux:

    # Create the directory for this workshop
    mkdir flask-workshop
    cd flask-workshop
    # Create a Python 3.3 virtualenv under the 'venv' directory
    virtualenv --python=python3.3 venv
    # Activate the virtual environment
    source venv/bin/activate
	
On Windows:

    # Create the directory for this workshop
    mkdir flask-workshop
    cd flask-workshop
    # Create a Python 3.3 virtualenv under the 'venv' directory
    C:\Python33\Scripts\virtualenv venv
    # Activate the virtual environment
    venv\Scripts\activate

The last step, _activate_ sets your terminal/command prompt session for using the Python installation in the `flask-workshop` directory. If you start up a new terminal then you will need to repeat the activation step again.

The `deactivate` command can be used to return your terminal back to normal. But for now let's leave it activated because it's time to install Flask.

# Installing Flask

So far as website frameworks go, Flask has a minimal number of libraries that it needs to run. Though it would be possible to find and install all these libraries manually it is much easier to use the `pip` command.

    pip install flask

