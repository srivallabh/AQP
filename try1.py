x = [ "isunit1.txt" , "isunit2.txt" , "isunit3.txt" , "isunit4.txt" , "isunit5.txt" ]
for each_file in x:
   with open(each_file,'a') as fo:
      fo.write('hiiiiiii')       
