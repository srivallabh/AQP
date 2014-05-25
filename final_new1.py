#!C:\Python27\python
import cgi,cgitb
import re

print "Content-type: text/html\n\n"
print"<html><body>"

form = cgi.FieldStorage()

college = form.getvalue('college')
subjects = form.getvalue('subjects')
branch = form.getvalue('branch')
subcode = form.getvalue('subcode')
credits = form.getvalue('credits')
exam = form.getvalue('exam')
qtype = form.getvalue('qtype')
print"<center><p><h1> %s </h1></p></center>" % college
print"<center><p><h1> %s </h1></p></center>" % branch
print"<p><h2> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SUB CODE : %s   &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      SUBJECT : %s  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREDITS : %s  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DATE : 5/MAY/2014 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; EXAM : %s  </p></h2> " %(subcode,subjects,credits,exam) 
print"<center><p><h1> %s questions</h1></p></center>" % qtype
class Blooms:
   
   def sentence_extractor(self):
      
      global_string = ""
      #print"<center><p><h1> %s </h1></p></center>" % len(subjects.strip())
      mysub = subjects.strip()
      #print"<center><p><h1> %s </h1></p></center>" % mysub
      if (mysub == 'Business Intelligence'):
         fname = 'biunit1.txt'
      elif(mysub == 'Software Engineering'):
         fname = 'se_unit1.txt'
      elif(mysub == 'Information Systems'):
         fname = 'isunit1.txt'
      elif(mysub == 'Operating Systems'):
         fname = 'osunit1.txt'
      elif(mysub == 'Software Testing'):
         fname = 'unitst.txt'
      else:
         fname = "none"
      qn = 0
      qs = 0
      qe = 0
      #print"<center><p><h1> %s </h1></p></center>" % len('Business Intelligence')
      #print"<center><p><h1> %s </h1></p></center>" % fname
      with open(fname,'r+') as fo:
         for line in fo:
            global_string+=line
      every_first=re.split('\|\|\|',global_string)
      all_questions = []
      map_word={'award':'evaluation','choose':'evaluation','conclude':'evaluation','criticize':'evaluation','decide':'evaluation','give':'evaluation','defend':'evaluation','determine':'evaluation','dispute':'evaluation','evaluate':'evaluation','judge':'evaluation','justify':'evaluation','measure':'evaluation','compare':'evaluation','mark':'evaluation','rate':'evaluation','recommend':'evaluation','ruleon':'evaluation','select':'evaluation','agree':'evaluation','interpret':'evaluation','explain':'evaluation','appraise':'evaluation','prioritize':'evaluation','opinion':'evaluation','support':'evaluation','importance':'evaluation','criteria':'evaluation','prove':'evaluation','disprove':'evaluation','assess':'evaluation','influence':'evaluation','perceive':'evaluation','value':'evaluation','estimate':'evaluation','influence':'evaluation','deduct':'evaluation','classify':'analysis','analyze':'analysis','compare':'analysis','contrast':'analysis','distinguish':'analysis','infer':'analysis','separate':'analysis','explain':'analysis','select':'analysis','categorize':'analysis','connect':'analysis','differentiate':'analysis','discriminate':'analysis','divide':'analysis','order':'analysis','point':'analysis','prioritize':'analysis','subdivide':'analysis','survey':'analysis','advertise':'analysis','appraise':'analysis','breakdown':'analysis','calculate':'analysis','conclude':'analysis','correlate':'analysis','criticize':'analysis','deduce':'analysis','devise':'analysis','diagram':'analysis','dissect':'analysis','estimate':'analysis','evaluate':'analysis','experiment':'analysis','focus':'analysis','illustrate':'analysis','organize':'analysis','outline':'analysis','plan':'analysis','question':'analysis','test':'analysis','apply':'application','build':'application','choose':'application','construct':'application','develop':'application','interview':'application','make':'application','organize':'application','experiment':'application','with':'application','plan':'application','select':'application','solve':'application','utilize':'application','model':'application','identify':'application','experiment':'application','solve':'application','apply':'application','illustrate':'application','modify':'application','use':'application','calculate':'application','change':'application','choose':'application','demonstrate':'application','discover':'application','experiment':'application','relate':'application','show':'application','sketch':'application','complete':'application','construct':'application','dramatize':'application','interpret':'application','manipulate':'application','paint':'application','prepare':'application','produce':'application','report':'application','teach':'application','act':'application','administer':'application','articulate':'application','chart':'application','collect':'application','compute':'application','determine':'application','develop':'application','employ':'application','establish':'application','examine':'application','explain':'application','interview':'application','judge':'application','list':'application','operate':'application','practice':'application','predict':'application','record':'application','schedule':'application','simulate':'application','transfer':'application','write':'application','compare':'comprehension','contrast':'comprehension','demonstrate':'comprehension','interpret':'comprehension','explain':'comprehension','extend':'comprehension','illustrate':'comprehension','infer':'comprehension','outline':'comprehension','relate':'comprehension','rephrase':'comprehension','translate':'comprehension','summarize':'comprehension','show':'comprehension','classify':'comprehension','who':'knowledge','what':'knowledge','why':'knowledge','when':'knowledge','omit':'knowledge','where':'knowledge','which':'knowledge','choose':'knowledge','find':'knowledge','how':'knowledge','define':'knowledge','label':'knowledge','show':'knowledge','spell':'knowledge','list':'knowledge','match':'knowledge','name':'knowledge','relate':'knowledge','tell':'knowledge','recall':'knowledge','select':'knowledge','define':'knowledge','identify':'knowledge','describe':'knowledge','briefly':'knowledge','draw':'knowledge','label':'knowledge','list':'knowledge','name':'knowledge','state':'knowledge','match':'knowledge','recognize':'knowledge','select':'knowledge','examine':'knowledge','locate':'knowledge','memorize':'knowledge','quote':'knowledge','recall':'knowledge','reproduce':'knowledge','tabulate':'knowledge','tell':'knowledge','copy':'knowledge','discover':'knowledge','duplicate':'knowledge','enumerate':'knowledge','listen':'knowledge','observe':'knowledge','omit':'knowledge','read':'knowledge','recite':'knowledge','record':'knowledge','repeat':'knowledge','retell':'knowledge','visualize':'knowledge','build':'synthesis','choose':'synthesis','combine':'synthesis','compile':'synthesis','compose':'synthesis','construct':'synthesis','create':'synthesis','design':'synthesis','develop':'synthesis','estimate':'synthesis','formulate':'synthesis','imagine':'synthesis','invent':'synthesis','makeup':'synthesis','originate':'synthesis','plan':'synthesis','predict':'synthesis','propose':'synthesis','solve':'synthesis','solution':'synthesis','suppose':'synthesis','discuss':'synthesis','modify':'synthesis','change':'synthesis','original':'synthesis','improve':'synthesis','adapt':'synthesis','minimize':'synthesis','maximize':'synthesis','delete':'synthesis','theorize':'synthesis','elaborate':'synthesis','test':'synthesis','improve':'synthesis','happen':'synthesis','change':'synthesis'} 
      for question in every_first:
         temp_string = question
         question_split=re.split(' ',temp_string)
	 	
         pattern = '[A-Z]\w+'
         keys_in_current = []   
         evalu = []
         analys = []
         app = []
         compre = []
         know = []
         synt = []
         
         for cap_word in question_split:
            if(re.match(pattern,cap_word)):
               capital_word = cap_word   
               if(len(capital_word)>0):
                  keys_in_current.append(capital_word)
            else:
               continue
	 
         for word_cap in keys_in_current:
            newest_word = word_cap.lower()     
            if map_word.has_key(newest_word):
               interim_var=map_word[newest_word]
	       if qtype == "Knowledge":
	          if(interim_var is 'knowledge'):
			with open("know.txt", "a") as myfile:
			        qn = qn + 1
				myfile.write(str(qn) + '.'+question + '(Knowledge)'+'      - 10m' + '\n')
				imed4 =  str(qn) + "." + question + '(Knowledge)' + '  -10 marks '   
				print "<h2> %s</h2>" % (imed4)     
               
		  else:
			continue
	       if qtype == "Synthesis":
		  if(interim_var is 'synthesis'):
			with open("synth.txt", "a") as myfile:
			        qs = qs + 1
				myfile.write(str(qs) + '.'+question + '(Synthesis)'+'      - 10m' + '\n')
				imed3 = str(qs) + '.'+ question + '(Synthesis)' + '  -10 marks '   
				print "<h2> %s</h2>" % (imed3)     
               
		  else:
			continue
	       if qtype == "Evaluation":
		  if(interim_var is 'evaluation'):
			with open("eval.txt", "a") as myfile:
			        qe = qe + 1
				myfile.write(str(qe) + '.'+question + '(Evaluation)'+'      - 10m' + '\n')
				imed3 =  str(qe) + '.'+question + '(Evaluation)' + '  -10 marks '   
				print "<h2> %s</h2>" % (imed3)     
               
		  else:
			continue  		
	       else:
	          continue

mybloom = Blooms()
mybloom.sentence_extractor()
print" Thank You!" 
print"<a href='http://localhost/bks/welcome1.php'>BACK</a>"
print "</body></html> "
