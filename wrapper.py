#!/usr/bin/env python
# coding=utf-8
#!/usr/bin/env python
#coding=utf-8
import requests
import json
import pprint
import random
"""
OxfordD is a wrapper for the oxford dictionary api, currently you can retrieve definitions,
example sentences, antonyms, synonyms, pronunciations and words
"""
class OxfordD:


    def __init__(self,url,app_id,app_key,language,word_id ="default",filters="default"):
        self.response_format = "json"
        self.url = url
        self.app_id = app_id
        self.app_key = app_key
        self.language = language
        self.word_id = word_id
        self.filters = filters

    #validate that the parameters exist and are of the write type
    def validate():
        if isinstance(self.url, basestring) == false:
            raise Exception('should be a string')
        if isinstance(self.app_id,basestring) == false:
            raise Exception('id should be a string')
        if isinstance(self.app_key,basestring) == false:
            raise Exception('key should be a string')
        if isinstance(self.language, basestring) == false:
            raise Exception('language should be a string')
        if isinstance(self.word_id,basestring) == false:
            raise Exception('word should be a string')


    #given a word retrieve its definition from the api
    def get_definition(self,word):
        self.word = word
        self.filters = 'definitions'
        self.url = self.url + "entries/" + self.language + '/' + self.word_id.lower() + '/' + self.filters
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            array = dict['results']
            dictionary = array[0]
            arrayS = dictionary['lexicalEntries']
            dictionaryT = arrayS[0]
            arrayU = dictionaryT['entries']
            dictionaryU = arrayU[0]
            arrayV = dictionaryU['senses']
            dictionaryW = arrayV[0]
            arrayW = dictionaryW['definitions']
            print(arrayW[0])
            return arrayW[0]
        if r.status_code == 400:
            print("not found")
            return('not found')
        if r.status_code == 404:
            print("not found")
            return('not found')



    #given a word retrieve its pronunciation from the api
    def get_pronunciation(self,word):
        self.word = word
        self.filters = 'pronunciations'
        self.url = self.url + "entries/" + self.language + '/' + self.word_id.lower() + '/' + self.filters
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            arrayA = dict['results']
            dictA = arrayA[0]
            arrayB = dictA['lexicalEntries']
            dictB = arrayB[0]
            arrayC = dictB['pronunciations']
            dictC = arrayC[0]
            print(dictC['phoneticSpelling'])
            return dictC['phoneticSpelling']
        if r.status_code == 400:
            print("not found")
            return('not found')
        if r.status_code == 404:
            print("not found")
            return('not found')


    #given a word retrieve a sentence that uses the word
    def get_example(self,word):
        self.word = word
        self.filters = 'examples'
        self.url = self.url + "entries/" + self.language + '/' + self.word_id.lower() + '/' + self.filters
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            arraya = dict['results']
            dicta = arraya[0]
            arrayb = dicta['lexicalEntries']
            dictb = arrayb[0]
            arrayc = dictb['entries']
            dictc = arrayc[0]
            arrayd = dictc['senses']
            dictd = arrayd[0]
            arraye = dictd['examples']
            dicte = arraye[0]
            print(dicte['text'])
            return dicte['text']
        if r.status_code == 400:
            print("not found")
            return('not found')
        if r.status_code == 404:
            print("not found")
            return('not found')


    #will generate a random word from the words in in the oxford api wordslist
    def get_random_word(self):
        self.url = self.url + "wordlist/" + self.language + '/' + "registers=Rare"
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            arraya = dict['results']
            index = random.randint(0,1000)
            dicta = arraya[index]
            return(dicta['word'])
        if r.status_code == 400:
            print("not found")
            return('not found')
        if r.status_code == 404:
            print("not found")
            return('not found')


    #will provide an antonym for a given word
    def get_antonym(self,word): 
        self.word = word
        self.url = self.url + "entries/" + self.language + '/' + self.word_id.lower() + "/synonyms;antonyms"
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            array = dict['results']
            dicta = array[0]
            array1 = dicta['lexicalEntries']
            dict2 = array1[0]
            array2 = dict2['entries']
            dict3 = array2[0]
            array3 = dict3['senses']
            dict4 = array3[0]
            array4 = dict4['antonyms']
            dict5 = array4[0]
            return dict5['text']
        if r.status_code == 400:
            print("not found")
            return('not found')
        if r.status_code == 404:
            print("not found")
            return('not found')


    #will provide a synonym for a given word
    def get_synonym(self,word):
        self.word = word
        self.url = self.url + "entries/" + self.language + '/' + self.word_id.lower() + "/synonyms;antonyms"
        r = requests.get(self.url, headers = {'app_id':self.app_id, 'app_key': self.app_key})
        if r.status_code == 200:
            dict = json.loads(r.text)
            array = dict['results']
            dicta = array[0]
            array1 = dicta['lexicalEntries']
            dict2 = array1[0]
            array2 = dict2['entries']
            dict3 = array2[0]
            array3 = dict3['senses']
            dict4 = array3[0]
            array4 = dict4['subsenses']
            dict5 = array4[0]
            array5 = dict5['synonyms']
            dict6 = array5[0]
            return dict6['text']
        if r.status_code == 400:
            print("not found")
            return("not found")
        if r.status_code == 404:
            print("not found")
            return("not found")