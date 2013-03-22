---
layout: ots
title: README 
---

Site can be viewed [here](http://opentechschool.github.com/python-flask)

This is a friendly how-to for contributors to the Websites with Python Flask course at OpenTechSchool. First, a quick refresher on the course:

> Ever wanted to learn how websites work or wanted to build one yourself? Or maybe you have played around with some HTML but wonder how to get it to actually do something? Now is the time to start with our Websites with Python Flask workshop. We'll take you through creating a basic interactive website using Flask, a very popular choice for websites created using the Python programming language.

> You will only need a laptop and a very basic understanding of Python (such as from our Introduction to Programming workshop). If you have previous experience with HTML, CSS and JavaScript then that is great too (but not required).

So we are expecting users who have written a little code before but never shared it. They may have some JS, Python or Ruby skills, and may have written a bit of HTML and CSS. We won't be expecting them to have Python installed when they show up.

# Class format

At OpenTechSchool we tend to go *practical* and *at your own pace*.

Practical meaning that we aren't big on theory, or requiring that people understand something completely before using it. We aren't expecting any of the students to become computer scientists. Generally programming for our students is a way of solving some practical problem. If they want to accomplish it with LISP or a spreadsheet is entirely up to them.

At your own pace means that we provide access to the complete course notes at the beginning of the session. Then students can progress individually. Some students will get through very quickly, others will take some time, and most will finish the core work with time to spare. The core work should be completable by everyone. To keep things interesting we supply various additional topics which are entirely optional.

A class schedule looks like this:

    1200 - Students still arriving, writing name tags, setting up laptops.
    1230 - Introductions, wifi instructions and location of coursework.
    1235 - Students learn stuff.
    1545 - Thankyous, maybe demonstrations.

As you can see, the schedule just has a big chunk of 'learn stuff'. We like to keep things open.

# Author Guide

So, fork this repository. The guide is written as a [Jekyll](http://jekyllrb.com/) site, hosted on GitHub pages. It's set up so you can just write pages in Markdown.  A markup guide is below.

Course work goes under `core/` or `extras/`. It's all linked together by `index.md` in the root direcory.

* `core/` covers the basic goals of the course. In this course that means setting up Git, creating a GitHub account, creating a repo, etc etc. Put any images in `core/images/`
* `extras/` are all the interesting things people can do once they have completed the basics. Things like hosting with Heroku, or sending emails.

It's easiest to start at the end. Think of a fun and interesting topic to add to the extras. Then you can copy this file to get an idea for formatting.

## Editing Text

We use long-lines (no newlines in paragraphs) to keep diffs moderately sane.

I use Emacs 24, with markdown-mode (Ubuntu emacs-goodies-el) and gfm-mode (GitHub markdown minor-mode). Set `longlines-show-hard-newlines` if you want to see where all the newlines are.

# Markup Guide

# First level section
## Second level section
### Third level section
#### Fourth level section

* List item
  * Sub item
  * Sub item 2
* List it m 2

1. Ordered list item
2. Ordered list item 2
3. Ordered list item 3
  * Sub item 1
  * Sub item 2
4. Ordered list item 4
  1. Ordered sub item 1
  2. Ordered sub item 2
5. Ordered list item 5


*emphasis text* for emphasis

**strong text** for strong

Getting literal with `backticks`

    Or use an indent of 4 spaces, 
	to get yourself a code block, 
	that looks lovely.

> Do a bit of blockquoting. You can still reflow the text as much as you like.  Newlines are awesome.  And made of win.

[links for nerds](http://slashdot.org)

[links for internal stuff](section8.html)

This is a horizonal rule:

******

If you want to highlight some ruby code:

    def foo
        puts 'foo'
    end

Bit of command line:

    $ holla holla
    get dolla
    $ 

For a more complete list of languages see [highlight.js](http://softwaremaniacs.org/media/soft/highlight/test.html)
