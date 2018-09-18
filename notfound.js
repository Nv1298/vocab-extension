//for all the strings which are "not found" (if any), replace with an empty string
for(i = 0; i < wordsL.length; i++){
	if(wordsL[i] == "not found"){
		wordsL[i] = " ";
	}
}

for(i = 0; i < pronunc.length; i++){
	if(pronunc[i] == "not found"){
		pronunc[i] = " ";
	}
}

for(i = 0; i < defL.length; i++){
	if(defL[i] == "not found"){
		defL[i] = " ";
	}
}

for(i = 0; i < synL.length; i++){
	if(synL[i] == "not found"){
		synL[i] = " ";
	}
}

for(i = 0; i < antL.length; i++){
	if(antL[i] == "not found"){
		antL[i] = " ";
	}
}

for(i = 0; i < sentL.length; i++){
	if(sentL[i] == "not found"){
		sentL[i] = " ";
	}
}