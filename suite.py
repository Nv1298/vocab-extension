#!/usr/bin/env/python
import os
from executor import Executor
from wrapper import OxfordD
"""
This file will get pronunciations from the api to populate the extension.
The pronunciations will be written to  javascript files to be used later on
"""
e = Executor("placeholder","placeholder")
e.change_name()
name = e.get_varname()
word = e.get_word()
ox = OxfordD('https://od-api.oxforddictionaries.com/api/v1/','8f27772c','058491c3348d8a03d687c9d84d7c5515','en')


#initialize an array in the javascript file to hold the pronunciations
createPr = "var pronunc = [];\n"
#add pronunciations to the array after they are retrieved
text = "pronunc.push(" + "\"" + ox.get_pronunciation(word) + "\"" + ';\n'

filename = "pronunciations.js"
if os.path.exists(filename):
	file = open(filename,"a")
	file.write(text)
else:
	file = open(filename,"w")
	file.write(createPr)		#only initialze the array if it is the first time writing to the file
	file.write(text)