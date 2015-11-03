#!/bin/python 
# Author: IAB
# purpose: Demo the string manipulation

import string

msg = "fuck yeah, im doing great it seems \n"
print "The Original Message is: ", msg 
print "Length of Message is: ", len(msg)

print "Gonna print some range of Message is:", msg[0:4]

print "Going through UPPER case:", string.upper(msg)
print "Going through lower case:", string.lower(msg)

print "Gonna split the string: ", string.split(msg)
print "Gonna join the string: ", string.join(msg)

print "Gonna capitalize the string: ", string.capitalize(msg)
print "Gonna Capword the string: ", string.capwords(msg)

msg2 = "Fuck Yeah\n"
print "Gonna campare the msg/msg2 two string\n"
print "Actual content of msg2 is: ", msg2
if msg != msg2:
 print "They NOT same\n"

print "Im gonna loop the msg2 string here\n"
for letter in msg2:
 print letter
