import nltk
import re 
class Retrieve:
    def fileio(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   

   
a = Retrieve()
file_as_string=a.fileio()
'''print file_as_string'''

every_first=re.split('\|\|\|',file_as_string)
'''print every_first'''
for word in every_first:
	
