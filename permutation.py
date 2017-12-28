#!/usr/bin/env python

def permutations(s):
	
	plist = []

	if len(s) == 1:
		plist = [s]
	
	else:
		#for every letter and its index in String:
		for i,let in enumerate(s):
			print let
			
			#for every permutation of the string left:
			for left_string in permutations(s[:i] + s[i+1:]):
				
				print "i: {} and let+left_string is: {} + {} ".format(i,let,left_string)
				plist += [let+left_string]
				print plist
				print "---------------------------------"

	return plist


print permutations("abc")