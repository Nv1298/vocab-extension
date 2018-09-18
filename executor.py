#!/usr/bin/env python
# coding=utf-8
from wrapper import OxfordD
ox = OxfordD('<url>','<app_id>','<app_key>','en','placeholder','definitions')

class Executor:
    def __init__(self,word,varname):
       self.word = word
	   self.varname = varname
	
    def change_name(self):
	   self.word = ox.get_random_word()
	   self.varname = self.word 
	
    def get_varname(self):
        return self.varname

    def get_word(self):
        return self.word