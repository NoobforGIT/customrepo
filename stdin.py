#!/bin/python
# Author : IAmBee
# Purpose : STDIN example

name = raw_input("What is your Name: ")
age = input("What is Your Age? ")
expect = input("What do you think that How long you gonna live? ")
org = expect - age
print "\n"
print "Hello", name, "!!\n"
print "As you said, you gonna live ",expect, "Years !\n"
print "BTW, You gonna live for another", org, "years only ! Hurry UP !\n"
