#!/usr/bin/env/python
import os
from executor import Executor
from wrapper import OxfordD

"""
This file will synonyms from the api to populate the extension.
The synonyms will be written to  javascript files to be used later on
"""

#call executor class to generate a random word from the api
e = Executor("placeholder","placeholder")
e.change_name()
word = e.get_word()
ox = OxfordD('https://od-api.oxforddictionaries.com/api/v1/','8f27772c','058491c3348d8a03d687c9d84d7c5515','en')

#initialize an array in the javascript file to store the synonyms
createArray = "var " + "synL" + " = " + "[]" + ";\n"
#push synonyms into the file after they are retrieved
text = "synL.push(" + ox.get_synonym(word) + ")" + ";\n"


filename = "synonym.js"
if os.path.exists(filename):
	file = open(filename,"a")
	file.write(text)
else:
	file = open(filename,"w")
	file.write(createArray)	#only initialize the array if it is the first time writing to the file
	file.write(text)