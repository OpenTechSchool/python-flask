---

layout: ots
title: HTML, CSS and JavaScript

---

Websites can be roughly divided into two parts, the browser and the server.

We are all familiar with web browsers, you are using one right now. There are a number of popular ones, such as Chrome, Firefox and Internet Explorer.

All web browsers handle the four fundamental technologies of the web:

## HTML

The HyperText Markup Language. This is a file containing most of the text content of a web page and has a `.html` extension. The text is wrapped in _tags_ to give them meaning. A snippet of HTML might look like this:

	<blockquote>"Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness"."</blockquote>
	<div class="cite">John Green</div>

And when the browser _renders_ the HTML it looks like this:

<div style="padding: 30px;">
<blockquote>"Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness"."</blockquote>
<div class="cite">John Green</div>
</div>


## CSS

Cascading Style Sheets give the browser styling hints for the HTML. It has a `.css` extension. Every website has CSS, because HTML looks _absolutely terrible_ without it.

For the quote above we can do a stylesheet like this:

     blockquote {
		 background-color: black;
		 color: yellow;
		 padding: 10px;
	 }
	 
	 .cite {
		 text-align: right;
		 font-weight: bold;
		 font-size: x-large;
	 }

Each section in the stylesheet applies to a different set of tags. The first section applies to any ``blockquote`` tags. The second section applies to any tags which have the attribute ``class="cite"`` as part of their name (like the second tag in the example.)

When applied, this "styles" the quote to look like this:

<div style="padding: 30px;">
<blockquote style="background-color: black; color: yellow; padding: 10px;">"Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness"."</blockquote>
<div class="cite" style="text-align: right; font-weight: bold; font-size: x-large;">John Green</div>
</div>

Note that even though the default style is terrible, that doesn't stop me from creating an alternate, equally ugly, style.

## JavaScript

JavaScript is an entire programming language contained entirely within the browser. Though HTML with CSS might look pretty, it can't actually do anything once the page has been rendered.


This snippet of JavaScript will run in your browser and scan the current page for `blockquote` tags and give them a random color every 200 milliseconds (five times per second).

    function partypartyparty(event) {
	  var blockquotes = document.getElementsByTagName('blockquote');
	  for(var i=0; i<blockquotes.length; i++) {
	    var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var e = blockquotes[i];
		e.style.setProperty('color', 'rgb('+r+','+g+','+b+')');
	  }

	  window.setTimeout(party.partypartyparty, 200);
    };

If you add it to the page then the result is, well, startling:

<div style="padding: 30px;">
<blockquote class="fancyquote" style="background-color: black; color: yellow; padding: 10px;">"Nerds like us are allowed to be unironically enthusiastic about stuff. Nerds are allowed to love stuff - like, jump-up-and-down-in-your-chair-can't-control-yourself love it. When people call other people nerds, mostly what they're saying is "You like stuff", which is not a good insult at all. Like, "You are too enthusiastic about the miracle of human consciousness"."</blockquote>
<div class="cite" style="text-align: right; font-weight: bold; font-size: x-large;">John Green</div>
</div>

We won't be covering JavaScript in this workshop, but if you do end up doing one of our JavaScript workshops in future then you will find much more useful things to do with it.

<script type="text/javascript" src="js/partypartyparty.js"> </script>
