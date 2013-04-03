---

layout: ots
title: Professional CSS

---

Once you are comfortable with CSS rules and properties you might start to wonder how the professionals use it. There is actually a big difference between learning CSS and using it. When learning you usually just put some CSS rules into a single file and leave it at that. But a real website might have many hundreds of rules combined with some strict design requirements and a need for cross-browser compatibility. Combine that with having to be understood and kept up-to-date by a team of developers and you have got yourself quite a challenge.

## CSS Frameworks

CSS Frameworks make it easier to manage styles for these larger, more complicated websites. All usually have the same key features:

**Style reset**.  Internet Explorer's `<h3>` tag might not look the same as Google Chrome's `<h3>` tag. Frameworks start their CSS with a bunch of directives redefining most HTML tags to a common styling.

**Grid Layout**. You may be wondering how we get websites with multiple columns and nice box layouts. Traditionally it was all done with manual `<div>` styling. But now frameworks define a grid layout, usually with something like 12 columns per row.

Here is an example of a two-column layout:


	<div class="row">
		<div class="column-3">Left sidebar</div>
		<div class="column-9">Main content</div>
	</div>

**Typographical reset**. This is a font reset that looks a little more pleasing to the eye. It sets things like line spacing and font size.

**Form styles**. Because the default form buttons and input boxes look boring these days.
**Extra components**. Many frameworks provide things like a menu bar system that can turn a `<ul>` tag into a pretty menu, or styled boxes for showing `<img>` tags in.

Learning a framework is similar to learning something like Flask. It can be a lot of work to get started, but over time it enables you to do things a lot quicker and still keep a decent amount of control. Things like a properly maintained grid system can save days of headaches with cross-browser compatibility.

Here are some of the more popular frameworks used today:

* [Twitter Bootstrap](http://twitter.github.com/bootstrap/) is one of the most popular. In some ways it has redefined what a standard web page looks like.
* [Foundation](http://foundation.zurb.com/) is a good, fully featured alternative that works great with SASS css.
* [Blueprint](http://www.blueprintcss.org/) is a bit older but very mature.
* [YUI](http://yuilibrary.com/) comes from the Yahoo team. It's very comprehensive and covers a lot of JavaScript as well. You might like to play with the [grid builder](http://yui.github.com/gridbuilder/).
* [1140](http://cssgrid.net/) is a contemporary 12-grid system for those who want just a little grid magic.

Finally, there is a great compilation website comparing some of the most popular frameworks [here](http://usablica.github.com/front-end-frameworks/compare.html)!

## CSS Languages

There are in fact a few entire languages that are dedicated to CSS. These languages are more powerful than CSS, often allowing things like variables and templates, but are compiled down to regular CSS files for hosting.

A common problem is how to deal with colours. For example if you had a corporate colour scheme of `#3311FF` your CSS would be littered with `#3311FF` references:

	.nav { background-color: #3311FF; }
	.button { border-color: #3311FF; }
	.cake .icing { color: #3311FF; }

In a CSS language you would be able to use a variable instead:

	$corporate_color: #3311FF;
	.nav { background-color: $corporate_color; }
	.button { border-color: $corporate_color; }
	.cake .icing { color: $corporate_color; }

Use of a CSS language is very common in large websites these days. Here are some of the more popular ones in use today:

* [SASS](http://sass-lang.com/) is one of the original CSS languages. It uses the Ruby programming language under the hood. You might like to try the [Python](https://pypi.python.org/pypi/pyScss/1.1.5) port which is compatible with SASS 3.2. You can also take a look at [Compass](http://compass-style.org/) which pushes SASS even further.
* [LESS](http://lesscss.org/) has a very similar philosophy. It is written in JavaScript, so it can either be run in the browser or, using Node, on the server.
