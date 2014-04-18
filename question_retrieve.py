__author__ = 'Srivallabh'
__guidance__ = 'Naresh E'

'''from retrieve import Retrieve_Sentence'''

import re
import nltk
from nltk.tokenize import RegexpTokenizer
''' Class to retrieve questions individually '''
class Retrieve_Sentence:
    
	

    def sentence_extractor(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   
''' class to retrieve words '''
class Retrieve_Question(Retrieve_Sentence):
	def question_extractor(self):
		capword_tokenizer = RegexpTokenizer('[A-Z]\w+')		
		b = Retrieve_Sentence()	
		file_as_string=b.sentence_extractor()	
		every_first=re.split('\|\|\|',file_as_string)
		for question in every_first:
			temp_string = question
			question_split=re.split(' ',temp_string)			
			'''first_word=nltk.word_tokenize(temp_string)'''
			for cap_word in question_split:			
				capital_word=capword_tokenizer.tokenize(cap_word)
				print capital_word		
			
a = Retrieve_Question()
a.question_extractor()
