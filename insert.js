var def = "<b>Definition: </b>";
var ex = "<b>Example: </b>";
var pr = "<b>Pronunciation: </b>";
var syn = "<b>Synonyms: </b>";
var ant = "<b>Antonyms: </b>";

//add all the data retrieved from the api into html file
window.addEventListener("click", function(event) {
	document.getElementById('card1').innerHTML = def + defL[0] + "<br/>" + "<br/>" + ex + sentL[0] + "<br/>" + "<br/>" + pr + pronunc[0];
	document.getElementById('card2').innerHTML = def + defL[1] + "<br/>" + "<br/>" + ex + sentL[1] + "<br/>" + "<br/>" + pr + pronunc[1];
	document.getElementById('card3').innerHTML = def + defL[2] + "<br/>" + "<br/>" + ex + sentL[2] + "<br/>" + "<br/>" + pr + pronunc[2];
	document.getElementById('card4').innerHTML = def + defL[3] + "<br/>" + "<br/>" + ex + sentL[3] + "<br/>" + "<br/>" + pr + pronunc[3];
	document.getElementById('card5').innerHTML = def + defL[4] + "<br/>" + "<br/>" + ex + sentL[4] + "<br/>" + "<br/>" + pr + pronunc[4];
	document.getElementById('card6').innerHTML = def + defL[5] + "<br/>" + "<br/>" + ex + sentL[5] + "<br/>" + "<br/>" + pr + pronunc[5];

	document.getElementById('word1').innerHTML = wordsL[0];
	document.getElementById('word2').innerHTML = wordsL[1];
	document.getElementById('word3').innerHTML = wordsL[2];
	document.getElementById('word4').innerHTML = wordsL[3];
	document.getElementById('word5').innerHTML = wordsL[4];
	document.getElementById('word6').innerHTML = wordsL[5];

	document.getElementById('slider1').innerHTML = syn + synL[0] + "<br/>" + "<br/>" + ant + antL[0];
	document.getElementById('slider2').innerHTML = syn + synL[1] + "<br/>" + "<br/>" + ant + antL[1];
	document.getElementById('slider3').innerHTML = syn + synL[2] + "<br/>" + "<br/>" + ant + antL[2];
	document.getElementById('slider4').innerHTML = syn + synL[3] + "<br/>" + "<br/>" + ant + antL[3];
	document.getElementById('slider5').innerHTML = syn + synL[4] + "<br/>" + "<br/>" + ant + antL[4];
	document.getElementById('slider6').innerHTML = syn + synL[5] + "<br/>" + "<br/>" + ant + antL[5];

});



