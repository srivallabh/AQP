import nltk
import re 


class Retrieve_Sentence:


    def sentence_extractor(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   

a = Retrieve_Sentence()
file_as_string=a.sentence_extractor()
print file_as_string
''' Function retrieveing individual questions 
    def question_extractor(self):
	b = Retrieve()	
	file_as_string=b.sentence_extractor()	
	every_first=re.split('\|\|\|',file_as_string)
	for word in every_first:
		print word


a = Retrieve()
a.question_extractor()'''
'''print file_as_string

every_first=re.split('\|\|\|',file_as_string)
for word in every_first:
	print word'''
