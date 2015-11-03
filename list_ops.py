#!/bin/python 
#Author: IAM
#Purpose: Playing with "LIST" in python 

import string

range(11)
print "printing som number ranges", range(1,10)

stringlist = ["Yo", "How", "You", "Doing"]

print "The actual string list:", stringlist 

stringlist.reverse()

print "Printing the reverse of stringlist:", stringlist

strlist2 = ["God", "Damn", "it"]

print "Printing the 2nd new stringlist: ", strlist2

stringlist.append(strlist2)
print "Let's append the 2nd string list to 1st: ", stringlist

stringlist.pop()

print "Popping the strlist2 from 1st list: ", stringlist

stringlist.extend(strlist2)

print "Extending the strlist with 2nd list: ", stringlist

print "Let do some insertion to our string list (Zero, One)"

stringlist.insert(0,"Zero")
stringlist.insert(1,"One")

print "Here we go out brand new stringlist: ", stringlist

print "Lets do some log file related stuff\n"
mylog = "20151004 12.12.12.123 110 12.32.32.32 80 404 indextml"

print "Below is mylog: \n", mylog

print "Type of mulog is: ", type(mylog)

print "Lets spilt to mylog"

mylog2 = string.split(mylog)

print "So what is the type of new mylog2 then: ", type(mylog2)

print "Here is the myolg2 content:\n", mylog2

print "Get some range from the mylog2 list: ", mylog2[2:4]

mylog3 = mylog2[2:4]
mylog3 = string.join(mylog3)
print "Ok, Lets make the range intems into string: ", mylog3
