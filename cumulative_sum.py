#!/usr/bin/env python

# Return cumulative sum from 0 to the integer. For ex, if n=4, sum=4+3+2+1
def cumul_sum(n):
	if n == 0:
		return 0
	else:
		while n>0:
			return n+cumul_sum(n-1)
			

print cumul_sum(5)
"""
print 15%4
print 134%10
print 1000%10
print 134//10
"""
# Given an integer, create a function that returns a sum of individual 
# digits in that integer. For ex, if n=4321, return 4+3+2+1

def sum_indiv(n):
	if len(str(n)) == 1:
		return n
	else:
		while n>0:
			return n%10+sum_indiv(n//10)
			

print sum_indiv(54865)	

print 134/10
print 134//10
print 134/10.0
print 134//10.0

"""
Create a function called word_split() which takes in a string phrase 
and a set list_of_words. The function will then determine if it is 
possible to split the string in a way in which words can be made 
from the list of words. You can assume the phrase will only contain 
words found in the dictionary if it is completely splittable.

For example: 

word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
['i', 'love', 'dogs', 'John']

word_split('themanran',['clown','ran','man'])
[]
"""
def word_split(phrase,list_of_words,output=None):
	if output is None:
		output = []
	
	for word in list_of_words:
		if phrase.startswith(word):
			output.append(word)
			return word_split(phrase[len(word):],list_of_words,output)

	return output




print word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])



