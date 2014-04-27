'''from retrieve import Retrieve_Sentence'''
import re
import nltk
from nltk.tokenize import RegexpTokenizer

class Retrieve_Sentence:
    
	

    def sentence_extractor(self):
        global_string = ""              
        with open("st1.txt",'r+') as fo:
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
		map_word={'award':'evaluation','choose':'evaluation','conclude':'evaluation','criticize':'evaluation','decide':'evaluation','give':'evaluation','defend':'evaluation','determine':'evaluation','dispute':'evaluation','evaluate':'evaluation','judge':'evaluation','justify':'evaluation','measure':'evaluation','compare':'evaluation','mark':'evaluation','rate':'evaluation','recommend':'evaluation','ruleon':'evaluation','select':'evaluation','agree':'evaluation','interpret':'evaluation','explain':'evaluation','appraise':'evaluation','prioritize':'evaluation','opinion':'evaluation','support':'evaluation','importance':'evaluation','criteria':'evaluation','prove':'evaluation','disprove':'evaluation','assess':'evaluation','influence':'evaluation','perceive':'evaluation','value':'evaluation','estimate':'evaluation','influence':'evaluation','deduct':'evaluation','classify':'analysis','analyze':'analysis','compare':'analysis','contrast':'analysis','distinguish':'analysis','infer':'analysis','separate':'analysis','explain':'analysis','select':'analysis','categorize':'analysis','connect':'analysis','differentiate':'analysis','discriminate':'analysis','divide':'analysis','order':'analysis','point':'analysis','prioritize':'analysis','subdivide':'analysis','survey':'analysis','advertise':'analysis','appraise':'analysis','breakdown':'analysis','calculate':'analysis','conclude':'analysis','correlate':'analysis','criticize':'analysis','deduce':'analysis','devise':'analysis','diagram':'analysis','dissect':'analysis','estimate':'analysis','evaluate':'analysis','experiment':'analysis','focus':'analysis','illustrate':'analysis','organize':'analysis','outline':'analysis','plan':'analysis','question':'analysis','test':'analysis','apply':'application','build':'application','choose':'application','construct':'application','develop':'application','interview':'application','make':'application','organize':'application','experiment':'application','with':'application','plan':'application','select':'application','solve':'application','utilize':'application','model':'application','identify':'application','experiment':'application','solve':'application','apply':'application','illustrate':'application','modify':'application','use':'application','calculate':'application','change':'application','choose':'application','demonstrate':'application','discover':'application','experiment':'application','relate':'application','show':'application','sketch':'application','complete':'application','construct':'application','dramatize':'application','interpret':'application','manipulate':'application','paint':'application','prepare':'application','produce':'application','report':'application','teach':'application','act':'application','administer':'application','articulate':'application','chart':'application','collect':'application','compute':'application','determine':'application','develop':'application','employ':'application','establish':'application','examine':'application','explain':'application','interview':'application','judge':'application','list':'application','operate':'application','practice':'application','predict':'application','record':'application','schedule':'application','simulate':'application','transfer':'application','write':'application','compare':'comprehension','contrast':'comprehension','demonstrate':'comprehension','interpret':'comprehension','explain':'comprehension','extend':'comprehension','illustrate':'comprehension','infer':'comprehension','outline':'comprehension','relate':'comprehension','rephrase':'comprehension','translate':'comprehension','summarize':'comprehension','show':'comprehension','classify':'comprehension','who':'knowledge','what':'knowledge','why':'knowledge','when':'knowledge','omit':'knowledge','where':'knowledge','which':'knowledge','choose':'knowledge','find':'knowledge','how':'knowledge','define':'knowledge','label':'knowledge','show':'knowledge','spell':'knowledge','list':'knowledge','match':'knowledge','name':'knowledge','relate':'knowledge','tell':'knowledge','recall':'knowledge','select':'knowledge','define':'knowledge','identify':'knowledge','describe':'knowledge','briefly':'knowledge','draw':'knowledge','label':'knowledge','list':'knowledge','name':'knowledge','state':'knowledge','match':'knowledge','recognize':'knowledge','select':'knowledge','examine':'knowledge','locate':'knowledge','memorize':'knowledge','quote':'knowledge','recall':'knowledge','reproduce':'knowledge','tabulate':'knowledge','tell':'knowledge','copy':'knowledge','discover':'knowledge','duplicate':'knowledge','enumerate':'knowledge','listen':'knowledge','observe':'knowledge','omit':'knowledge','read':'knowledge','recite':'knowledge','record':'knowledge','repeat':'knowledge','retell':'knowledge','visualize':'knowledge','build':'synthesis','choose':'synthesis','combine':'synthesis','compile':'synthesis','compose':'synthesis','construct':'synthesis','create':'synthesis','design':'synthesis','develop':'synthesis','estimate':'synthesis','formulate':'synthesis','imagine':'synthesis','invent':'synthesis','makeup':'synthesis','originate':'synthesis','plan':'synthesis','predict':'synthesis','propose':'synthesis','solve':'synthesis','solution':'synthesis','suppose':'synthesis','discuss':'synthesis','modify':'synthesis','change':'synthesis','original':'synthesis','improve':'synthesis','adapt':'synthesis','minimize':'synthesis','maximize':'synthesis','delete':'synthesis','theorize':'synthesis','elaborate':'synthesis','test':'synthesis','improve':'synthesis','happen':'synthesis','change':'synthesis'} 

		for question in every_first:

			temp_string = question 
			question_split=re.split(' ',temp_string)			
			
			#print question_split
			#all_questions.append(question_split)
		#print all_questions
			keys_in_current = []
			evalu = []
			analys = []
			app =[]
			compre = []
			know = []
			synt = []
			for cap_word in question_split:			
                		capital_word=capword_tokenizer.tokenize(cap_word)
				if(len(capital_word)>0):
					keys_in_current.append(capital_word)
				#for any_cap_word in capital_word:
			#print keys_in_current
			for word_cap in keys_in_current:
				for removing_brack in word_cap:
					removing_brackstr = str(removing_brack)					
					#print map_word[ '\''+ removing_brackstr + '\'']					
					#new_word= '\'' + removing_brackstr + '\''	
					#newer_word = str(new_word)
					#newest_word = newer_word.lower()
					newest_word = removing_brackstr.lower()
					#print newest_word
					interim_var=map_word[newest_word]
					if(interim_var is 'evaluation'):
						evalu.append(question)
					elif(interim_var is 'analysis'):
						analys.append(question)
					elif(interim_var is 'application'):
						app.append(question)
					elif(interim_var is 'comprehension'):
						compre.append(question)
					elif(interim_var is 'knowledge'):
						know.append(question)
					else:
						synt.append(question)					
			print "evaluation", evalu ;
			print "analysis",analys ;
			print "application",app ;
			print "comprehension",compre ;
			print "knowledge",know;
			print "synthesis",synt;		
					#print (map_word.get(newer_word))					
					#print(map_word.get('"' + removing_brackstr + '"'))
					#var=map_word[removing_brack]
					#print var
			#keys_in_current = []
						
			
						
				
a = Retrieve_Question()
a.question_extractor()
