
	
			
"""
4.1 Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the
two subtrees of any node never differ by more than one.
"""

class tree41(object):
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		
	def add(self,data):
		if self.data == None:
			self.data = data
		else:
			if data <= self.data:
				if self.left == None:
					self.left = tree41(data)
				else:
					self.left.add(data)
			else:
				if self.right == None:
					self.right = tree41(data)
				else:
					self.right.add(data)
	
	def show(self):
		import collections
		QQ = collections.deque()
		
		level = 0
		QQ.append((level,self))
		last_level = level
		while QQ:
			level,node = QQ.popleft()
			
			if last_level != level:
				print ""
			last_level = level
				
			print node.data if node else "X",
			
			if node:
				QQ.append((level+1,node.left))
				QQ.append((level+1,node.right))

			
def check_tree_balance(root):
	if root == None:
		return 0, True
	
	
	left, lret = check_tree_balance(root.left)
	right, rret = check_tree_balance(root.right)
	
	if abs(left-right) > 1:
		return max(left,right)+1,False
	else:
		return max(left,right)+1,True
	
	
def main_check_balance():
	nums = [4,2,6,1,3,5,7,7,7,7]
	root = tree41()
	for n in nums:
		root.add(n)
		
	root.show()
	
	print "\n",check_tree_balance(root)
		
	
	
	
	
	
			
		
			
		
		
		
				 	
		
		



"""
4.2 Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.
"""


"""
[CLS] DO-AGAIN
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
[CLS]:DO AGAIN : find up till the first left-childed parent
4.6 Write an algorithm to find the'next'node (i.e., in-order successor) of a given node
in a binary search tree. You may assume that each node has a link to its parent.
"""


"""
4.7 Design an algorithm and write code to find the first common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE:
This is not necessarily a binary search tree.
"""



"""
4.8 You have two very large binary trees: T1, with millions of nodes, and T2, with
hundreds of nodes. Create an algorithm to decide if T2 is a subtree of Tl.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of
n is identical to T2. That is, if you cut off the tree at node n, the two trees would
be identical.
"""

	

"""
4.9 You are given a binary tree in which each node contains a value. Design an algorithm
to print all paths which sum to a given value. The path does not need to
start or end at the root or a leaf.
"""

	
	

"""
[CLS]
construct a bin tree from in-order & pre-order sequence
in[]   = {4, 8, 2, 5, 1, 6, 3, 7}
post[] = {8, 4, 5, 2, 6, 7, 3, 1} 
Output : Root of below tree
          1
       /     \
     2        3
   /    \   /   \
  4     5   6    7
    \
      8
"""

if __name__ == "__main__":
	main_check_balance()
	
	print "Done\n"
