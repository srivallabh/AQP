#!C:\Python27\python
import cgi,cgitb
import re
import os
import random
print "Content-type: text/html\n\n"
print"<html><body>"
form = cgi.FieldStorage()
college = form.getvalue('college')
subjects = form.getvalue('subjects')
branch = form.getvalue('branch')
subcode = form.getvalue('subcode')
credits = form.getvalue('credits')
exam = form.getvalue('exam')

print"<center><p><h1> %s </h1></p></center>" % college
print"<center><p><h1> %s </h1></p></center>" % branch
print"<p><h2> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SUB CODE : %s   &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      SUBJECT : %s  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREDITS : %s  &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DATE : 5/MAY/2014 &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; EXAM : %s  </p></h2> " %(subcode,subjects,credits,exam) 
class Blooms:
   def sentence_extractor(self):
      unit1qs = ""
      unit2qs = ""
      unit3qs = ""
      unit4qs = ""
      unit5qs = ""
      fname = ""
      mysub = ""
      #print"<center><p><h1> UNIT-1 </h1></p></center>"
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
      
      #print"<center><p><h1> %s </h1></p></center>" % len('Business Intelligence')
      #print"<center><p><h1> %s </h1></p></center>" % fname
      with open(fname,'r+') as fo:
         for line in fo:
            unit1qs+=line
      every_first=re.split('\|\|\|',unit1qs)
      all_questions = []
      map_word={'award':'evaluation','choose':'evaluation','conclude':'evaluation','criticize':'evaluation','decide':'evaluation','give':'evaluation','defend':'evaluation','determine':'evaluation','dispute':'evaluation','evaluate':'evaluation','judge':'evaluation','justify':'evaluation','measure':'evaluation','compare':'evaluation','mark':'evaluation','rate':'evaluation','recommend':'evaluation','ruleon':'evaluation','select':'evaluation','agree':'evaluation','interpret':'evaluation','explain':'evaluation','appraise':'evaluation','prioritize':'evaluation','opinion':'evaluation','support':'evaluation','importance':'evaluation','criteria':'evaluation','prove':'evaluation','disprove':'evaluation','assess':'evaluation','influence':'evaluation','perceive':'evaluation','value':'evaluation','estimate':'evaluation','influence':'evaluation','deduct':'evaluation','classify':'analysis','analyze':'analysis','compare':'analysis','contrast':'analysis','distinguish':'analysis','infer':'analysis','separate':'analysis','explain':'analysis','select':'analysis','categorize':'analysis','connect':'analysis','differentiate':'analysis','discriminate':'analysis','divide':'analysis','order':'analysis','point':'analysis','prioritize':'analysis','subdivide':'analysis','survey':'analysis','advertise':'analysis','appraise':'analysis','breakdown':'analysis','calculate':'analysis','conclude':'analysis','correlate':'analysis','criticize':'analysis','deduce':'analysis','devise':'analysis','diagram':'analysis','dissect':'analysis','estimate':'analysis','evaluate':'analysis','experiment':'analysis','focus':'analysis','illustrate':'analysis','organize':'analysis','outline':'analysis','plan':'analysis','question':'analysis','test':'analysis','apply':'application','build':'application','choose':'application','construct':'application','develop':'application','interview':'application','make':'application','organize':'application','experiment':'application','with':'application','plan':'application','select':'application','solve':'application','utilize':'application','model':'application','identify':'application','experiment':'application','solve':'application','apply':'application','illustrate':'application','modify':'application','use':'application','calculate':'application','change':'application','choose':'application','demonstrate':'application','discover':'application','experiment':'application','relate':'application','show':'application','sketch':'application','complete':'application','construct':'application','dramatize':'application','interpret':'application','manipulate':'application','paint':'application','prepare':'application','produce':'application','report':'application','teach':'application','act':'application','administer':'application','articulate':'application','chart':'application','collect':'application','compute':'application','determine':'application','develop':'application','employ':'application','establish':'application','examine':'application','explain':'application','interview':'application','judge':'application','list':'application','operate':'application','practice':'application','predict':'application','record':'application','schedule':'application','simulate':'application','transfer':'application','write':'application','compare':'comprehension','contrast':'comprehension','demonstrate':'comprehension','interpret':'comprehension','explain':'comprehension','extend':'comprehension','illustrate':'comprehension','infer':'comprehension','outline':'comprehension','relate':'comprehension','rephrase':'comprehension','translate':'comprehension','summarize':'comprehension','show':'comprehension','classify':'comprehension','who':'knowledge','what':'knowledge','why':'knowledge','when':'knowledge','omit':'knowledge','where':'knowledge','which':'knowledge','choose':'knowledge','find':'knowledge','how':'knowledge','define':'knowledge','label':'knowledge','show':'knowledge','spell':'knowledge','list':'knowledge','match':'knowledge','name':'knowledge','relate':'knowledge','tell':'knowledge','recall':'knowledge','select':'knowledge','define':'knowledge','identify':'knowledge','describe':'knowledge','briefly':'knowledge','draw':'knowledge','label':'knowledge','list':'knowledge','name':'knowledge','state':'knowledge','match':'knowledge','recognize':'knowledge','select':'knowledge','examine':'knowledge','locate':'knowledge','memorize':'knowledge','quote':'knowledge','recall':'knowledge','reproduce':'knowledge','tabulate':'knowledge','tell':'knowledge','copy':'knowledge','discover':'knowledge','duplicate':'knowledge','enumerate':'knowledge','listen':'knowledge','observe':'knowledge','omit':'knowledge','read':'knowledge','recite':'knowledge','record':'knowledge','repeat':'knowledge','retell':'knowledge','visualize':'knowledge','build':'synthesis','choose':'synthesis','combine':'synthesis','compile':'synthesis','compose':'synthesis','construct':'synthesis','create':'synthesis','design':'synthesis','develop':'synthesis','estimate':'synthesis','formulate':'synthesis','imagine':'synthesis','invent':'synthesis','makeup':'synthesis','originate':'synthesis','plan':'synthesis','predict':'synthesis','propose':'synthesis','solve':'synthesis','solution':'synthesis','suppose':'synthesis','discuss':'synthesis','modify':'synthesis','change':'synthesis','original':'synthesis','improve':'synthesis','adapt':'synthesis','minimize':'synthesis','maximize':'synthesis','delete':'synthesis','theorize':'synthesis','elaborate':'synthesis','test':'synthesis','improve':'synthesis','happen':'synthesis','change':'synthesis'} 
      count_eval = 0
      count_anal = 0
      count_appl = 0
      count_comp = 0
      count_know = 0
      count_synth = 0
      qcount = 0
      qkount = 0
      meval = []
      anal = []
      appl = []
      compre = []
      know = []
      synth = []
      selected_know = []
      for question in every_first:
         temp_string = question
	 question_split=re.split(' ',temp_string)
	 pattern = '[A-Z]\w+'
         keys_in_current = []   
         for cap_word in question_split:
            if(re.match(pattern,cap_word)):
               capital_word = cap_word   
               if(len(capital_word)>0):
                  keys_in_current.append(capital_word)
            else:
               continue
	 for word_cap in keys_in_current:
	    newest_word = word_cap.lower()
	    #print '1.',newest_word
	    if map_word.has_key(newest_word):
               interim_var=map_word[newest_word]
               qkount = qkount + 1
	       if(interim_var is 'evaluation'):
	          qe=question+' (Evaluation)'
	          meval.append(qe)
               elif(interim_var is 'analysis'):
	          qan=question+' (Analysis)'
	          anal.append(qan)
               elif(interim_var is 'application'):
	          qa=question+' (Application)'
	          appl.append(qa)
               elif(interim_var is 'comprehension'):
	          qc=question+' (Comprehension)'
	          compre.append(qc)
               elif(interim_var is 'knowledge'):
	          qk=question+' (Knowledege)'
	          know.append(qk)
               else:
	          qs=question+' (Synthesis)'
	          synth.append(qs)
                  
	       #print "********************************************",'\n'
	 
            else:
	        continue
	    #if ( qkount > 5 ):
	        #os.exit
            #print "meval=",meval
	    #print "anal=",anal
	    #print "appl",appl
	    #print "compre=",compre
	    #print "know=",know
	    #print "synth=",synth
	    merged_list = meval + anal + appl + compre + know + synth
	    
	    #print "merged=",merged_list
	    qc = 0
	    qqc = 0
	    marks = ""
	    if (exam == 'CIE'):
	        marks = '5 marks'
		qqc = 5
	    elif(exam == 'SEE'):
	        marks = '10 marks'
		qqc = 10
	    else:
		marks = "0m"
      
      selected_questions=[]	
      while len(selected_questions)<qqc:
	    random.shuffle(merged_list)
            indx=random.randint(0,len(merged_list)-1)
            if merged_list[indx] not in selected_questions:
                selected_questions.append(merged_list[indx])
            else:
                pass
      #print selected_questions 
      with open("qpaper.txt", "a") as myfile:
            for index, ques in enumerate(selected_questions):
	        myfile.write(str(index+1)+'.'+ques+'  -'+marks + '\n')
		imed4 = str(index+1)+'.'+ques+'  -'+marks
		print "<h2>%s</h2>" %(imed4)
	    
mybloom = Blooms()
mybloom.sentence_extractor()
print" Thank You!" 
print"<a href='http://localhost/bks/welcome1.php'>BACK</a>"
print "</body></html> "
