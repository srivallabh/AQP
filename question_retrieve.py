'''from retrieve import Retrieve_Sentence'''
import re
import nltk
from nltk.tokenize import RegexpTokenizer

class Retrieve_Sentence:
    
	

    def sentence_extractor(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   

class Retrieve_Question(Retrieve_Sentence):
	

	def question_extractor(self):
		capword_tokenizer = RegexpTokenizer('[A-Z]\w+')		
		b = Retrieve_Sentence()	
		file_as_string=b.sentence_extractor()	
		every_first=re.split('\|\|\|',file_as_string)
		#print every_first
		for question in every_first:

			temp_string = question
			question_split=re.split(' ',temp_string)			
			#print question_split
			
			for cap_word in question_split:			

				capital_word=capword_tokenizer.tokenize(cap_word)
				for any_cap_word in capital_word:
					print any_cap_word
						
				
a = Retrieve_Question()
a.question_extractor()
