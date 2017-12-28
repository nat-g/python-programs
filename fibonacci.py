#!/usr/bin/env python

def fin_rec(n):
	memoization = {}

	if n == 0 or n == 1:
		return 1

	elif n not in memoization:
		memoization[n] = fin_rec(n-1) + fin_rec(n-2)

	return memoization[n]

print fin_rec(5)
