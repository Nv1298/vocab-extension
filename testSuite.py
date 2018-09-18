#!/usr/bin/env python
import os
from executor import Executor
from wrapper import OxfordD
"""
This file will get definitions and words from the api to populate the extension.
The words and definitions will be written to  javascript files to be used later on
"""

#call the executor class to generate a random word for the variable name and to enter into the api
e = Executor("placeholder","placeholder")
e.change_name()
name = e.get_varname()
word = e.get_word()
ox = OxfordD('<your_url>','app_id','app_key','en')


#define arrays in the javascript file to hold all of the definitions and words
createDefinitions = "var defL = [];"
createWord = "var wordsL = [];"

#push the retrieved words and definitions into the array
text = "defL.push(" + "\""+ ox.get_definition(word) + "\"" + ");\n"
assignation = "wordsL.push(" + "\""+ word + "\"" + ");\n"

#javascript files that the words and definitions will be read to
wordsfile = "words.js"
filename = "definitions.js"

#write the text to the respective javscript files
if os.path.exists(wordsfile):
	wfile = open(wordsfile, "a")
	wfile.write(assignation)
	if os.path.exists(filename):
		file = open(filename,"a")
		file.write(text)
	else:
		file = open(filename,"w")
		file.write(createDefinitions)	#new array is only initialized if it is the first time writing to file
		file.write(text)
else:
	wfile = open(wordsfile,"w")
	wfile.write(createWord)				#new array is only initialized if it is the first time writing to file
	wfile.write(assignation)
	if os.path.exists(filename):
		file = open(filename,"a")
		file.write(text)
	else:
		file = open(filename,"w")
		file.write(createDefinitions)
		file.write(text)
