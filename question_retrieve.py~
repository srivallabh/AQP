'''from retrieve import Retrieve_Sentence'''
import re
import nltk


class Retrieve_Sentence:
    
	

    def sentence_extractor(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   

class Retrieve_Question(Retrieve_Sentence):
	def question_extractor(self):
		b = Retrieve_Sentence()	
		file_as_string=b.sentence_extractor()	
		every_first=re.split('\|\|\|',file_as_string)
		for word in every_first:
			print word

a = Retrieve_Question()
a.question_extractor()
