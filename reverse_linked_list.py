#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def reverse_linked_list(node):
	prevnode = None
	nextnode = None

	while node.nextnode:
		nextnode = node.nextnode 
		node.nextnode = prevnode
		prevnode = node
		node = nextnode

	return node
