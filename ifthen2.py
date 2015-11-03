#!/usr/bin/python
#Author : IAB
#Purpose: If then PArt II

import sys
#print sys.argv

max = 2
# Since running "python script_name.py" that is the reason im subtracting one
# If the script in the executable modethen no need to do this operation 

actual = len(sys.argv)-1

#print max
print actual

if actual < max:
	print "You required,", max, "but actually you have", actual
elif actual == 2:
	print "Shit man, your count is fine", max , actual
elif actual > max and actual <= 4:
	print "You are in Branch 2, means you have", actual ,"with you"
elif actual >= 7 and actual <=10:
	print "You are in to branch 3, means you have", actual , "with you"
else:
	print sys.argv[0], "has the limit of accepting the only 10 Args" 

