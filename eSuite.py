#!/usr/bin/env/python
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
ox = OxfordD('<your_url>','<app_id>','<app_key>','en')

#define an array in the javascript file to hold the example sentences
createArray = "var " + "sentL" + " = " + "[]" + ';'
#push the sentence retrived into the array
text = "sentL.push(" + ox.get_example(word) + ")" + ';\n'


filename = "examples.js"
if os.path.exists(filename):
	file = open(filename,"a")	
	file.write(createArray)	#only initilize array if it is the first time writing to the file
	file.write(text)
else:
	file = open(filename,"w")
	file.write(text)