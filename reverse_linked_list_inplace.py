#!/usr/bin/env python

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None


def countnodes(node):

	if node.isEmpty:
		return False
	else:
		count = 1
		while node.nextnode:
			count += 1
			node = node.nextnode

	return count


def last_to_the_end(n,node):
	
	number = countnodes(node)
	targetN = number - n + 1

	while targetN > 0:
		node = node.nextnode
		targetN -= 1

	return node
