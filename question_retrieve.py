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
		all_questions = []
		for question in every_first:

			temp_string = question
			question_split=re.split(' ',temp_string)			
			#print question_split
			#all_questions.append(question_split)
		#print all_questions
			keys_in_current = []
			for cap_word in question_split:			
                		capital_word=capword_tokenizer.tokenize(cap_word)
				if(len(capital_word)>0):
					keys_in_current.append(capital_word)
				#for any_cap_word in capital_word:
			print keys_in_current
			keys_in_current = []
						
			
						
				
a = Retrieve_Question()
a.question_extractor()
