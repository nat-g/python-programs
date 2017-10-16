#!/usr/bin/env python


#myTree = [ 'a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f',[],[]], []]]

myTree = [ 
	'a',  #root  
	['b', #left subtree 
		['d', [], []], #left subtree of the left subtree with 2 empty children
		['e', [], []]],  #right subtree of the left subtree with 2 empty children 
	['c', #right subtree 
		['f',[],[]], #left subtree of the right subtree with 2 empty children
		[]]    #right subtree of the right subtree with 2 empty children
	]


print (myTree)
print 'root  =  ', myTree[0]
print 'left subtree  =  ', myTree[1]
print 'right subtree  =  ', myTree[2]


def BinaryTree(r):
	return [r,[],[]]

def insertLeft(root, newBranch):
	t = root.pop(1) #pops root[1] which is the left child of the tree
	if len(t) > 1:
		root.insert(1, [newBranch,t,[]]) #Inserts left child newBranch and pushes previously existing child "t" as a left child of newBranch
	else:
		root.insert(1, [newBranch, [], []]) #Inserts an item at a given position - 1
	return root 

def insertRight(root, newBranch):
	t = root.pop(2) #pops root[2] which is the right child of the tree
	if len(t) > 1:
		root.insert(2, [newBranch,[], t]) #Inserts right child newBranch and pushes previously existing child "t" as a right child of newBranch
	else:
		root.insert(2, [newBranch, [], []]) #Inserts an item at a given position - 2
	return root 

def getRootVal(root):
	return root[0]

def setRootVal(root, newValue):
	root[0] = newValue

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print l




