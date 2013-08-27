function partypartyparty() {
    var quotes = document.getElementsByClassName('fancyquote');
    for(var i=0; i<quotes.length; i++) {
        var r = Math.floor(Math.random()*255);
        var g = Math.floor(Math.random()*255);
        var b = Math.floor(Math.random()*255);
        var q = quotes[i];
        q.style.setProperty('color', 'rgb('+ r +','+ g +',' + b + ')');
    }
}

window.setInterval(partypartyparty, 500);
