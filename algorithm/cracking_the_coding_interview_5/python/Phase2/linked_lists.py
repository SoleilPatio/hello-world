
"""
2.1 Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.last = self
        
    def append(self, data):
        new_node = Node(data)
        
        current = self.last
        while current.next != None:
            current = current.next
        current.next = new_node
        self.last = new_node
        
    def show(self):
        p = self
        
        while p:
            print p.data, "->",
            p = p.next
        print "nil"
        
        

def bubblesort_ll(head_node):
    
    bSwap = False
    prev_node = head_node
    current_node = head_node.next if head_node != None else None
    next_node = current_node.next if current_node != None else None
    nextnext_node = next_node.next if next_node != None else None
    
    while True:
        while next_node:
            if current_node.data > next_node.data:
                #swap
                bSwap = True
                prev_node.next = next_node
                next_node.next = current_node
                current_node.next = nextnext_node
                #update
                prev_node = next_node
                next_node = nextnext_node
                nextnext_node = nextnext_node.next if nextnext_node != None else None
                
            else:
                #update
                prev_node = current_node
                current_node = next_node
                next_node = nextnext_node
                nextnext_node = nextnext_node.next if nextnext_node != None else None
                
            head_node.show()
            
                
        if bSwap == False:
            break
        #prepare next loop
        bSwap = False
        prev_node = head_node
        current_node = head_node.next if head_node != None else None
        next_node = current_node.next if current_node != None else None
        nextnext_node = next_node.next if next_node != None else None
        
def selection_sort_ll(head):
    
    pc = head
    c  = pc.next if pc else None
    nc = c.next if c else None
    
    while c:
        ps = head
        s  = ps.next if ps else None
        ns = s.next if s else None
        
        b_insert = False
        while s != c and s != None:
            if c.data < s.data:
                b_insert = True
                #insert
                pc.next = nc
                ps.next = c
                c.next = s
                #update
                c = nc
                nc = c.next if c else None
                head.show()
                break
            else:
                ps = s
                s  = ps.next if ps else None
                ns = s.next if s else None
        
        #advance c
        if b_insert == False:
            pc = c
            c  = pc.next if pc else None
            nc = c.next if c else None
        
                 
def merge(left,right):
    
    head = Node()
    
    phead = head
    pleft = left.next
    pright = right.next
    while True:
        if pleft and pright:
            if pleft.data < pright.data:
                phead.next = pleft
                pleft = pleft.next
                phead = phead.next
                phead.next = None
            else:
                phead.next = pright
                pright = pright.next
                phead = phead.next
                phead.next = None
        elif pleft == None and pright == None:
            return head
        elif pleft == None and pright != None:
            phead.next = pright
            return head
        elif pright == None and pleft != None:
            phead.next = pleft
            return head
            
    return head
                
                
        
    
    
    
    
    
def merge_sort_ll(head):
    if head.next == None:
        return
    if head.next.next == None:
        return
    
    
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slowprv = slow
        slow = slow.next
        fast = fast.next.next
        
    left = head
    right = Node()
    right.next = slow.next
    slow.next = None
    
   
    
    merge_sort_ll(left)
    merge_sort_ll(right)
    
    new_head = merge(left,right)
    head.next = new_head.next
    
    
    
        
def remove_sorted_list(head):
    
    prev_n = head
    curr_n = prev_n.next if prev_n else None
    next_n = curr_n.next if curr_n else None
    
    while curr_n:
        if prev_n.data == curr_n.data:
            #remove curren_n
            prev_n.next = next_n
            #update
            curr_n = prev_n.next if prev_n else None
            next_n = curr_n.next if curr_n else None
        else:
            prev_n = curr_n
            curr_n = prev_n.next if prev_n else None
            next_n = curr_n.next if curr_n else None
        head.show()
            
        
                
        
def main_remove_duplicate():
    head = Node()
    head.append(5)
    head.append(6)
    head.append(1)
    head.append(8)
    head.append(3)
    head.append(3)
    head.append(0)
    head.append(8)
    head.append(5)
    head.append(6)
    head.append(1)
    head.append(8)
    head.show()
    
#     bubblesort_ll(head)
#     selection_sort_ll(head)
    merge_sort_ll(head)
    print "Sorted:"
    head.show()
    remove_sorted_list(head)
    print "Removed:"
    head.show()
    
    
    
    
    
    


"""
2.2 Implement an algorithm to find the kth to last element of a singly linked list.
"""
def find_last_k_helper(listhead, k, rank_from_start = 1):
    
    if listhead==None:
        return 0, None
    
    brank, ret = find_last_k_helper(listhead.next,k, rank_from_start+1)
    brank += 1
    if brank == k:
        return brank,  listhead.data
    else:
        return brank, ret
    


def main_find_last_k():
    head = Node()
    head.append(5)
    head.append(6)
    head.append(1)
    head.append(8)
    head.append(3)
    head.append(3)
    head.append(0)
    head.append(8)
    head.append(5)
    head.append(6)
    head.append(1)
    head.append(8)
    head.show()
    
    l, ret = find_last_k_helper(head, 4)
    print ret
    
    

"""
2.3 Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e
"""
class list23(object):
    def __init__(self, data=None):
        self.data=data
        self.next=None
        
    def append(self, data):
        
        node = self
        
        while node.next != None:
            node = node.next
            
        node.next = list23(data)
        return node.next
    
    def show(self):
        node = self
        
        while node != None:
            print node.data, "->",
            node = node.next
            
        
        
    
def del_list_node( node ):
    if node.next == None:
        return
    
    
    node.data = node.next.data
    node.next = node.next.next
    
    
        
def main_del_node():
    listhead = list23('a')
    listhead.append('b')
    nodec = listhead.append('c')
    listhead.append('d')
    listhead.append('e')
    
    listhead.show()
    del_list_node(nodec)
    listhead.show()
    
    
    
    
    
        


"""
2.4 Write code to partition a linked list around a value x, such that all nodes less than
x come before all nodes greater than or equal to x. 

[CLS][NOTE]:IT'S VERY HARD TO MOVE LINK OF SINGLE LINKED LIST!!!!!!!USE DATA SWAP!!
"""
class list24(object):
    def __init__(self, data=None):
        self.data = data
        self.link = None
        
    def append_data(self, data):
        
        node = self
        while node.link != None:
            node = node.link
            
        node.link = list24(data)
    
    def append_node(self, a_node):
        
        node = self
        while node.link != None:
            node = node.link
            
        node.link = a_node
        
    def extend(self, otherlist):
        node = self
        while node.link != None:
            node = node.link
            
        node.link = otherlist.link
        
    def show(self):
        node = self.link
        
        while node != None:
            print node.data,"->",
            node = node.link
            
        print "nil"
        
        
def partition_list(a_list, x):
    greater_list = list24()
    
    prev_node = a_list
    node = a_list.link
    while node != None:
        if node.data >= x:
            prev_node.link = node.link
            greater_list.append_node(node)
            node.link = None
            node = prev_node.link
        else:
            prev_node = node
            node = node.link
            
            
    a_list.show()
    greater_list.show()
    
    a_list.extend(greater_list)
    
    
def main_partition():
    
    a_list = list24()
    a_list.append_data(9)
    a_list.append_data(3)
    a_list.append_data(5)
    a_list.append_data(7)
    a_list.append_data(1)
    a_list.append_data(8)
    
    a_list.show()
    partition_list(a_list, 5)
    a_list.show()
            
            
        
        
    


"""
2.5 You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit is at the
head of the list. Write a function that adds the two numbers and returns the sum
as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
Output: 9 -> 1 -> 2.That is, 912.
"""


"""
2.6 Given a circular linked list, implement an algorithm which returns the node at
the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points
to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A - > B - > C - > D - > E - > C [the same C as earlier]
Output: C
"""

        

"""
2.7 Implement a function to check if a linked list is a palindrome
"""




if __name__ == "__main__":
#     main_remove_duplicate()
#     main_find_last_k()
#     main_partition()
    main_del_node()
