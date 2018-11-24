var seed = 3;
function random() {
    var x = Math.random() * 10000;
    return x - Math.floor(x);
}


function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    
    // While there remain elements to shuffle...
    while (0 != currentIndex) {
	      
	// Pick a remaining element...
	randomIndex = Math.floor(random() * currentIndex);
	currentIndex -= 1;
	
	// And swap it with the current element.
	temporaryValue = array[currentIndex];
	array[currentIndex] = array[randomIndex];
	array[randomIndex] = temporaryValue;
    }
    return array;
}


