#!/bin/python
#Author: IAM
#Purpose: If, else & math


centr = 100
name = raw_input("What is your Name: ")
age = input("What is Your Age? ")
expect = input("What do you think that How long you gonna live? ")
remain = input("So, How much left over than? ")

left = centr - age
print left
if remain == left:
	print "Bingo!", name, ",you are correct"
else:
	print "Fuck you", name, ",You are wrong"
