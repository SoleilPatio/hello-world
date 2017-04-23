class Queue(object):
	def __init__(self):
		self.list = []
		
	def Queue(self,data):
		self.list.append(data)
		
	def Dequeue(self):
		if len(self.list) == 0:
			return None
		else:
			data = self.list[0]
			del self.list[0]
			return data
	
	def count(self):
		return len(self.list)
			


class BinTree(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
	def AddNode(self, data):
		node = self
		while (True):
			if data < node.data:
				if (node.left == None):
					node.left = BinTree(data)
					break
				else:
					node = node.left
			else:
				if (node.right == None):
					node.right = BinTree(data)
					break
				else:
					node = node.right
		
	def Show(self):
		nodeq = Queue()
		level = 0
		nodeq.Queue((self,level))
		
		lastl = 0
		while(nodeq.count() > 0):
			node, l = nodeq.Dequeue()
			
			if(lastl != l):
				print ""
			lastl = l
			
			if(node != None):
				print node.data,
				nodeq.Queue((node.left, l+1))
				nodeq.Queue((node.right,l+1))
			else:
				print "X",
				
				
def main_my_tree_test():
	import numpy as np
	
	btree = None
	for data in np.random.randint(100,size=10):
		if btree == None:
			btree = BinTree(data)
		else:
			btree.AddNode(data)
		
	btree.Show()
	
			
"""
4.1 Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the
two subtrees of any node never differ by more than one.
"""

"""
4.2 Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.
"""

"""
4.3 Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""

"""
4.4 Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked
lists).
"""

"""
4.5 Implement a function to check if a binary tree is a binary search tree.
"""

"""
4.6 Write an algorithm to find the'next'node (i.e., in-order successor) of a given node
in a binary search tree. You may assume that each node has a link to its parent.
"""

"""
4.7 Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE:
This is not necessarily a binary search tree.
"""

"""
4.8 You have two very large binary trees: Tl, with millions of nodes, and T2, with
hundreds of nodes. Create an algorithm to decide ifT2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of
n is identical to T2. That is, if you cut off the tree at node n, the two trees would
be identical.
"""

"""
4.9 You are given a binary tree in which each node contains a value. Design an algorithm
to print all paths which sum to a given value. The path does not need to
start or end at the root or a leaf.
"""

		
		


if __name__ == "__main__":
	main_my_tree_test()
	print "\nDone"