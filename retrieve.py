import nltk
 
class Retrieve:
    def fileio(self):
        global_string = ""              
        with open("se.txt",'r+') as fo:
         	for line in fo:
                       global_string += line
        return global_string   
a = Retrieve()
print a.fileio()

