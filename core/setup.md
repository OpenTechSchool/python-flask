---

layout: ots
title: Setup

---

# Which Python?

For this workshop it is recommended to use Python 3.3, which the latest version of Flask is compatible with!

You can see what version of Python is installed by starting the Python interpreter. For example on Linux and OSX you can run the `python` command:

    $ python
    Python 2.7.6 (default, Nov 26 2013, 12:52:49) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

Here you can see it is version `2.7.3`. If you don't have Python installed or you have Python 2 then continue reading. It is very possible to use Flask with Python 2, but we recommend moving to the latest version of the language.

# Python 3.3+

If you don't have this installed then you can download it [**here**](http://python.org/download/). The latest version at the time of writing is 3.3.2.

* Windows: Choose one of the Installer packages - 'x86' if you have 32-bit Windows, or 'x86-64' if you have 64-bit Windows. Just ask if you're not sure which.
* Mac: You most likely want the 64-bit/32-bit Installer.
* Linux: most distributions will already have Python 2 installed, but you can install Python 3 using your system's package manager. For example, with Ubuntu, use `$ sudo apt-get install python3`.

# pip

Python comes with a lot of built-in functionality in the form of modules. For example, we used the `turtle` module in the Introduction to Programming course. However, Python doesn't come with everything you might need. You can extend Python by adding new modules, which come bundled up in *packages*.

The `pip` command uses the [Python Packages Index](https://pypi.python.org/pypi) to install new Python packages. This makes it super-easy to install Flask and other packages that you might want to use in future, for example [Twitter](https://pypi.python.org/pypi/twitter/1.9.1) (to access the Twitter API to request data about Twitter) or [bashplotlib](https://pypi.python.org/pypi/bashplotlib/0.4.4) (to plot data on a graph in your terminal.)

### Windows

To install pip on Windows, download and open [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py). This will install both [pip] and [setuptools] \(pip uses setuptools to install packages\).

You should have **pip** installed in Python's `Scripts` folder. In a command prompt (**cmd.exe**, used for running install command or python manually) you might not have python and its scripts in Windows' PATH; this essentially means when you type something like `pip install flask`, Windows won't be able find `pip`. To fix this, you can go to `C:\Python33\Tools\Scripts\` and run the `win_add2path.py` file.

[pip]: https://pypi.python.org/pypi/pip
[setuptools]: https://pypi.python.org/pypi/setuptools

### Mac OS X & Linux

The `pip` command might already be installed, try running `pip` in the command prompt. If that didn't work then try:

    $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    $ sudo python get-pip.py

On Mac OSX you might need to use an older version of `pip` to workaround errors in the Mac OSX installation of OpenSSL. Details [here](https://github.com/pypa/pip/issues/829). If you have any troubles please
ask!

# Virtualenv

This part isn't required for Flask, but its very useful if you think you'll ever work on more than one python project! You can skip over this section if you like, or come back to it later.

**virtualenv** makes it easy to use different packages, and even different versions of packages, and even different *pythons*, in your python projects. So you could have one project using Flask, another using Django, another using Bottle and they won't step all over each other, and you won't be confused for which project you installed which package.

Installing on Windows is as easy as:

    C:\> pip install virtualenv

On OS X and Linux, try

    $ sudo pip install virtualenv

Now that it is installed, we can set up a "virtual environment" for this workshop. This will keep Flask and it's dependencies contained to just this workshop:

On OSX and Linux:

    # Create the directory for this workshop
    $ mkdir flask-workshop
    $ cd flask-workshop
    # Create a Python 3 virtualenv under the 'flaskenv' directory
    $ virtualenv --python=python3 flaskenv
    # Activate the virtual environment
    $ source flaskenv/bin/activate

On Windows:

    # Create the directory for this workshop
    C:\> mkdir flask-workshop
    C:\> cd flask-workshop
    # Create a Python 3 virtualenv under the 'flaskenv' directory
    C:\> virtualenv flaskenv
    # Activate the virtual environment
    C:\> flaskenv\Scripts\activate

The last step, *activate* sets up your terminal/command prompt session for using a contained Python3 installation in the `flask-workshop` directory. If you start up a new terminal then you will need to repeat the activation step again.

The `deactivate` command can be used to return your terminal back to normal. But for now let's leave it activated because it's time to install Flask.

# Installing Flask

So far as website frameworks go, Flask has a minimal number of libraries that it needs to run. Though it would be possible to find and install all these libraries manually it is much easier to use the `pip` command.

Now that everything is set up, installing Flask is as easy as:

    pip install flask
