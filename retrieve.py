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
re.split('\|||','file_as_string',maxsplit=1)
