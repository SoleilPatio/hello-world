
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
    
    bubblesort_ll(head)
    print "Sorted:"
    head.show()
    remove_sorted_list(head)
    print "Removed:"
    head.show()
    
    
    
    
                
                
                
                
                
                
        
    
    
    
    


"""
2.2 Implement an algorithm to find the kth to last element of a singly linked list.
"""


"""
2.3 Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e
"""


"""
2.4 Write code to partition a linked list around a value x, such that all nodes less than
x come before all nodes greater than or equal to x. 

[CLS][NOTE]:IT'S VERY HARD TO MOVE LINK OF SINGLE LINKED LIST!!!!!!!USE DATA SWAP!!
"""



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
    main_remove_duplicate()
