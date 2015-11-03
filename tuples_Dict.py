#!/bin/python
#Author: IAM
#Purpose: Examples for Tuples and Dcitionaries
import string
print "Let's Do this !\n"
mylist = ['you', 'simply', 'what', 'to', 'do']
print "The mylist content: \n", mylist
print "Here the type of mylist: \n", type(mylist)

print "\nGonna Declare the tuples name called mytules"
mytuples = ('you', 'simply', 'what', 'to', 'do')
print "Let's print the mytuples content: \n", mytuples
print "So, What is the types then: ", type(mytuples)

#print "\n Gonna change the 2nd placed values as Yoyo in mytuples"
#mytuples[2] = "Yoyo"
#print "Let print the updated mytuples: \n", mytuples

print "\nTuples are unchangeable, if you trying to change the you will ending upda the error"
print "But you can play with the list"
print "You can try by uncommenting above block of code - to test tuples"

print "\nOk, Will declare the Dictionary now !"
mydict = {'Num' : 1, 'Age' : 25}
print "Printing the mydict content: \n ", mydict
print "Return the specific (Age) value: \n", mydict['Age']

print "\nGonna insert  the new KV pair"
mydict['newValue'] = 0
print "An update Dict as below: \n", mydict

print "\nGonna update the Age as 24"
mydict['Age'] = 24
print "An update Dict as below: \n", mydict

print "\nPrint only the keys from the Dict: ", mydict.keys()
print "\nPrint only the values from the Dict: ", mydict.values()

print "\nGonna delete the Num from dict: ", 
del mydict['Num']
print "An update Dict as below: \n", mydict

print "\nGonna loop the mydict content: "
for k,v in mydict.iteritems():
 print k,v

print "\n we are going to update some nested values to single KEY"
myprice = [100,200]
mydict['Newprice'] = myprice
print "An update Dict as below: \n", mydict

