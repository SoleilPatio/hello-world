from test.pystone import PtrGlb
from platform import node
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

def check_balanced(tree):
	if tree != None:
		is_l_balanced, l_count = check_balanced(tree.left)
		is_r_balanced, r_count = check_balanced(tree.right)
		is_balanced = True if abs(l_count-r_count) <= 1 else False
		return is_balanced, max(l_count, r_count) + 1
	else:
		return True, 0
		
def main_check_balanced():
	tree = None
	for data in [1,4,2,1,3,6,5,7]:
# 	for data in [4,2,1,3,6,5,7]:
		if tree == None:
			tree = BinTree(data)
		else:
			tree.AddNode(data)
			
	tree.Show()
	
	print "\nIs Balanced?", check_balanced(tree)
	
	

"""
4.2 Given a directed graph, design an algorithm to find out whether there is a route
between two nodes.
"""
import collections

def is_connected_bfs(graph, fr, to):
	bfs_que = collections.deque()
	
	path = [fr]
	bfs_que.append(path)
# 	while True:
	while bfs_que:
		if len(bfs_que) == 0:
			return False, None
		path = bfs_que.popleft()
		node = path[-1]
		if node == to:
			return True, path
		else:
			for adjacent in graph.get(node,[]):
				newpath = list(path)
				newpath.append(adjacent)
				bfs_que.append(newpath)
		

def main_is_connected():
	Graph = {
			1:[2,3],
			5:[3],
			6:[4],
			3:[4],
		}
	
	print is_connected_bfs(Graph, 1, 4)
	
	quetest = collections.deque([1,2,3,4,5,6,7,8])
	
	while quetest:
		print quetest.popleft()
	
	pass

			
		
		

"""
[CLS] DO-AGAIN
4.3 Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""
import numpy as np

class BinSearchTree(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
	def add(self, data):
		if self.data == None:
			self.data = data
			return
		
		if data < self.data:
			if self.left == None:
				self.left = BinSearchTree(data)
				return
			else:
				self.left.add(data)
		else:
			if self.right == None:
				self.right = BinSearchTree(data)
				return
			else:
				self.right.add(data)
			
	
	def show(self):
		import collections
		bfs_q = collections.deque()
		
		level = 0
		last_level = 0
		bfs_q.append((self,level))
		while bfs_q:
			node, level = bfs_q.popleft()
			if last_level != level:
				print ""
			if node != None:
				print node.data,
				bfs_q.append((node.left, level+1))
				bfs_q.append((node.right, level+1))
			else:
				print "X",
			
			last_level = level 	


def construct_bintree(tree, sort_array, fr, to):
	if fr == to:
		tree.add(sort_array[fr])
		print sort_array[fr]
		return
	
	if to - fr == 1:
		tree.add(sort_array[fr])
		print sort_array[fr]
		tree.add(sort_array[to])
		print sort_array[to]
		return
	
	
	mid = (fr + to) /2
	tree.add(sort_array[mid])
	print sort_array[mid]
	
	
	construct_bintree(tree, sort_array, fr, mid-1 if (mid-1 >= fr) else fr)
	construct_bintree(tree, sort_array, mid+1 if (mid+1 <= to) else to, to)
	
	
	
	
	

def main_construct_bintree():
	sort_array = np.array(range(11))
# 	sort_array = [4,2,1,3,6,5,7]
	
	print sort_array
	
	tree = None
	for x in sort_array:
		if tree == None:
			tree = BinSearchTree(x)
		else:
			tree.add(x)
	
	tree.show()
	
	print ""
	tree = BinSearchTree(None)
	construct_bintree(tree, sort_array, 0, len(sort_array)-1)
	print "------------------"
	tree.show()
	
	
	

"""
4.4 Given a binary tree, design an algorithm which creates a linked list of all the
nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked
lists).
"""
import collections
def create_level_list(btree):
	ret_lists = []
	bfs_q = collections.deque()
	
	head_node = btree.get("head",None)
	
	level = 0
	bfs_q.append((head_node, level))
	
	while bfs_q:
		node, level = bfs_q.popleft()
		
		if len(ret_lists) < (level+1):
			ret_lists.append([])
		ret_lists[level].append(node)
		
		for child in btree.get(node,[]):
			bfs_q.append((child, level+1))
			
	return ret_lists
	

def create_level_list_bfs(btree, lists, level=0, root="head"):
	
	if root == None:
		return
	
	if root == "head":
		root = btree.get("head", None)
		level = 0
		
	if len(lists) == level:
		lists.append([])
	
	lists[level].append(root)
	
	for child in btree.get(root, []):
		create_level_list_bfs(btree, lists, level+1, child)
	
	
	

def main_create_level_list():
	btree = {
			"head" : 0,
			0 : [1,2],
			1 : [3,4],
			2 : [5,6]
			}
	
	lists = create_level_list(btree)
	
	for list in lists:
		print list
	
	
	lists = []
	create_level_list_bfs(btree, lists)
	
	for list in lists:
		print list
		
		
		

"""
4.5 Implement a function to check if a binary tree is a binary search tree.
"""
def check_is_bin_search_tree(tree, node):
	
	my_result = True
	childs = tree.get(node,[])
	count = len(childs)
	if count == 0:
		left = None
		right = None
		return True
	elif count == 1:
		left = childs[0]
		right = None
		if left > node:
			my_result = False
	else:
		left = childs[0]
		right = childs[1]
		if left > node or node >= right:
			my_result = False
		
	if my_result == False:
		return False
	
	l_result = check_is_bin_search_tree(tree, left)
	r_result = check_is_bin_search_tree(tree, right)
	
	
	return l_result and r_result and my_result
		
	
	
	

def main_check_is_bin_search_tree():
	tree1 = {
			"head":4,
			4:[2,5],
			2:[1,3],
			5:[None,6]
			}
	
	print check_is_bin_search_tree(tree1, tree1["head"])
	
	tree1 = {
			"head":4,
			4:[2,5],
			2:[3,1],
			5:[None,None]
			}
	
	print check_is_bin_search_tree(tree1, tree1["head"])
	
	
	
	
"""
4.6 Write an algorithm to find the'next'node (i.e., in-order successor) of a given node
in a binary search tree. You may assume that each node has a link to its parent.
"""
class dbstree(object):
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None
		
	def add(self,data):
		if self.data == None:
			self.data = data
			return
		
		if data <= self.data:
			if self.left == None:
				self.left = dbstree(data)
				self.left.parent = self
			else:
				self.left.add(data)
		else:
			if self.right == None:
				self.right = dbstree(data)
				self.right.parent = self
			else:
				self.right.add(data)
				
	def left_most(self, node):
		if node == None:
			return None
					
		ptr = node
		while True:
			if ptr.left == None:
				return ptr
			else:
				ptr = ptr.left
				
	def next(self,node):
		if node == None:
			return None
			
		#if I am root or a right child
		if node.parent == None:
			return node.left_most(node.right)
		
		if node.parent.right == node:
			return node.left_most(node.right)
			
		#if I am a left child
		if node.parent.left == node:
			next_node = node.left_most(node.right)
			if next_node == None:
				next_node = node.parent
			return next_node
			
		
		
		
	def show(self):
		import collections
		level_q = collections.deque()
		
		level = 0
		last_level = level
		level_q.append((self,level))
		
		while level_q:
			node, level = level_q.popleft()
			
			if last_level != level:
				print ""
			
			if node == None:
				print "x",
			else:
				next_node = node.next(node)
				nn = str(next_node.data) if next_node != None else "x"
				print node.data,"(%s)"%nn,
				level_q.append((node.left, level+1))
				level_q.append((node.right, level+1))
				
			last_level = level
			
		print ""
			
		
		
		
def main_find_next():
	import numpy as np
	tree = dbstree()
	
	for d in np.random.randint(10,size=10):
		tree.add(d)
		
	tree.show()
	
	print "-------"
	
		



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
# 	main_my_tree_test()
# 	main_check_balanced()
# 	main_is_connected()
# 	main_construct_bintree()
# 	main_check_balanced()
# 	main_create_level_list()
# 	main_check_is_bin_search_tree()
	main_find_next()
	
	
	print "\nDone"