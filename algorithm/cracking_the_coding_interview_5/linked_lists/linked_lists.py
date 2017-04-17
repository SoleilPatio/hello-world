
class Node:
    def __init__(self, data):
        self.m_data = data
        self.m_next = None
    
    def append(self, node):
        head = self
        while(head.m_next != None):
            head = head.m_next
        head.m_next = node
        
    def traversal(self):
        head = self
        while(head != None):
            print head.m_data,"->",
            head = head.m_next
        print "null"

def test_link_list():
    
    head = Node(0)
    
    head.append(Node(1))
    head.append(Node(2))
    head.append(Node(3))
    head.append(Node(3))
    head.append(Node(2))
    head.append(Node(1))
    head.append(Node(4))
    head.append(Node(5))
    
    head.traversal()
    
    return head

def gen_test_link_list(data_list):
    head = Node(data_list[0])
    
    for i in range(1,len(data_list)):
        head.append(Node(data_list[i]))
        
    head.traversal()
    return head

    
"""
2.1 Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
def remove_duplicate_with_hash(head):
    dup = {}
    
    previous = None
    while(head != None):
        if head.m_data in dup.keys():
            previous.m_next = head.m_next
            head = previous.m_next
        else:
            dup[head.m_data] = 1
            previous =  head
        
            
def remove_duplicate_with_2pointers(head):
    p1 = head
    
    previous = None
    while(p1 != None):
        p2 = p1.m_next
        p2previous = p1
        while(p2 != None):
            if p1.m_data == p2.m_data:
                p2previous.m_next = p2.m_next
                p2 = p2previous.m_next
            else:
                p2previous = p2
                p2 = p2.m_next
        p1 = p1.m_next
    


def main_remove_duplicate():
    #soltion1
    head = test_link_list()
    remove_duplicate_with_hash(head)
    head.traversal()
    
    #solution 2
    head = test_link_list()
    remove_duplicate_with_2pointers(head)
    head.traversal()
    
    


"""
2.2 Implement an algorithm to find the kth to last element of a singly linked list.
"""
def find_kth_last_element(head, count):
    p1 = head
    p2 = head
    offset = count
    
    while( offset > 0):
        if p2 == None:
            return None
        p2 = p2.m_next
        offset -=1
        
    if p2 == None:
        return p1.m_data
    
    while(p2 != None):
        p2 = p2.m_next
        p1 = p1.m_next
        
    return p1.m_data
    
    
    
def find_kth_last_element_recursive(head, count):
    if head == None:
        return 0, None
    
    (i, ret_node) = find_kth_last_element_recursive(head.m_next, count)
    i = i+1
    
    if i == count:
        print head.m_data
        return i , head
        
    return i, ret_node
        
    
  
    



def main_find_kth_last_element():
    head = gen_test_link_list(range(30))
    
    print find_kth_last_element(head, 30)
    
    print "Recursive:"
    i,ret_node = find_kth_last_element_recursive(head, 2)
    print i, ":",ret_node.m_data
    
    

"""
2.3 Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.
EXAMPLE
Input: the node c from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a- >b- >d->e
"""
def delete_node(del_node):
    if del_node == None or del_node.m_next == None:
        return
    
    del_node.m_data = del_node.m_next.m_data
    del_node.m_next = del_node.m_next.m_next
    


def main_del_node():
    head = gen_test_link_list(range(30))
    
    i,ret_node = find_kth_last_element_recursive(head, 10)
    print ret_node.m_data
    
    delete_node(ret_node)
    
    head.traversal()
    
    pass
    
    

"""
2.4 Write code to partition a linked list around a value x, such that all nodes less than
x come before all nodes greater than or equal to x.
"""

"""
2.5 You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the Ts digit is at the
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
#     test_link_list()
#     main_remove_duplicate()
#     main_find_kth_last_element()
    main_del_node()
    
    
    
    print "-----Done"