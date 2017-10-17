#!/usr/bin/env python

"""
There are three commonly used patterns to visit all the nodes in a tree. 
The difference between these patterns is the order in which each node is visited.
---preorder---
In a preorder traversal, we visit the root node first, then 
recursively do a preorder traversal of the left subtree, followed 
by a recursive preorder traversal of the right subtree.
---inorder---
In an inorder traversal, we recursively do an inorder traversal on 
the left subtree, visit the root node, and finally do a recursive 
inorder traversal of the right subtree.
---postorder---
In a postorder traversal, we recursively do a postorder traversal of the
left subtree and the right subtree followed by a visit to the root node.
"""

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()


"""
The algorithm for the postorder traversal is nearly identical to preorder
except that we move the call to print to the end of the function.
"""
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal
