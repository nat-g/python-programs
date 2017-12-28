#!/usr/bin/env python

# Reverse a string using recursion

def reverse(s):

	nlist = []

	if len(s) == 1:
		return s
	else:
		for char in s:
			nlist.insert(0,char)
			reverse(s[1:])

	return ''.join(nlist)



print reverse("astring")


def reverse1(s):

	nlist = []

	if len(s) == 1:
		return s
	
	return reverse1(s[1:]) + s[0]

print reverse1("astring")


