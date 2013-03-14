(function(party, undefined) {

    party.partypartyparty = function(event) {
	var blockquotes = document.getElementsByClassName('fancyquote');
	for(var i=0; i<blockquotes.length; i++) {
            var r = Math.floor(Math.random()*255);
            var g = Math.floor(Math.random()*255);
            var b = Math.floor(Math.random()*255);
            var e = blockquotes[i];
	    e.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
	}
	
	window.setTimeout(party.partypartyparty, 200);
    };

}( window.party = window.party || {} ));

party.partypartyparty();
