#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def findcycle(node):
	prevNode = None

	while nextnode:
		if node.nextnode = prevNode:
			return False
		else:
			prevNode = node
			node = node.nextnode

	return True
	
