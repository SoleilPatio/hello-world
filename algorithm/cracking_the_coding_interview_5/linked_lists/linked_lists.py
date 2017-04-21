from _random import Random

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

[CLS][NOTE]:IT'S VERY HARD TO MOVE LINK OF SINGLE LINKED LIST!!!!!!!USE DATA SWAP!!
"""
import numpy as np
def gen_test_linked_list_random(count):
    head = Node(np.random.randint(count))
    for x in np.random.randint(count,size=count):
        head.append(Node(x))
    head.traversal()
    
    return head

def gen_test_linked_list_seq(count):
    head = Node(0)
    for x in range(1,count):
        head.append(Node(x))
    head.traversal()
    
    return head
    
def partition_list(head, num):
    rp = head
    pp = head #point to the end of less than
    
    while(rp != None):
        head.traversal()
        if rp.m_data < num:
            if rp != pp:
                #swap
                temp = pp.m_data
                pp.m_data = rp.m_data
                rp.m_data = temp
            pp = pp.m_next
            rp = rp.m_next
        else:
            rp = rp.m_next
            
    return head
    
    
def main_partition():
    head = gen_test_linked_list_random(20)
#     head = gen_test_linked_list_seq(20)
    head = partition_list(head,10)
    head.traversal()
    
    
    pass



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
def gen_list(d_list):
    if len(d_list) == 0:
        return None
    
    head = Node(d_list[0])
    for d in d_list[1:]:
        head.append(Node(d)) 
        
    head.traversal()
    return head

def sum_list( l1, l2):
    import math
    sum_list = None
    sum = 0
    carry = 0
    while( l1 != None or l2 != None or carry != 0):
        l1d = l1.m_data if l1 != None else 0
        l2d = l2.m_data if l2 != None else 0
        
        sum = l1d + l2d + carry
        
        if sum >= 10:
            carry = 1
            num = sum-10
        else:
            carry = 0
            num = sum

        if sum_list == None:
            sum_list = Node(num)
        else:
            sum_list.append(Node(num))
            
        
        l1 = l1.m_next if l1 != None else None
        l2 = l2.m_next if l2 != None else None
        
    return sum_list
    
    
def sum_list_reverse(l1,l2,sum):
    if(l1 == None ):
        return 0
     
    carry = sum_list_reverse(l1.m_next, l2.m_next, sum)
    
    l1d = l1.m_data
    l2d = l2.m_data
    
    sumd = l1d + l2d + carry
    
    if sumd >= 10:
        carry = 1
        num = sumd - 10
    else:
        carry = 0
        num = sumd
        
    sum_next = sum.m_next
    sum.m_next = Node(num)
    sum.m_next.m_next = sum_next
    
    return carry
        
    
     
    
    
    
def list_len(li):
    ret_len = 0
    while(li != None):
        ret_len += 1
        li = li.m_next
    return ret_len
    
    
def pad_list(l1,l2):
    l1len = list_len(l1)
    l2len = list_len(l2)
    
    if(l1len > l2len):
        diff = l1len-l2len
        while(diff > 0):
            newl2 = Node(0)
            newl2.m_next = l2
            l2 = newl2
            diff -= 1
    elif(l1len < l2len):
        diff = l2len-l1len
        while(diff > 0):
            newl1 = Node(0)
            newl1.m_next = l1
            l1 = newl1
            diff -= 1
    
    return (l1,l2)
        
    
    
    

def main_sum_list():
    l1 = gen_list([1,2,6,1,7])
    l2 = gen_list([2,9,5])
    
    sum = sum_list(l1,l2)
    sum.traversal()
    
    print "Part B:Reverse"
    #Part B: reverse
    (l1,l2) = pad_list(l1,l2)
    l1.traversal()
    l2.traversal()
    
    sum = Node(0)
    sum_list_reverse(l1,l2,sum)
    sum.traversal()

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

def check_circular(linklist):
    nodedict = {}
    
    while(linklist != None):
        if linklist in nodedict:
            nodedict[linklist] += 1
            break
        else:
            nodedict[linklist] = 1
        linklist = linklist.m_next
        
    for node in nodedict.keys():
        if nodedict[node] > 1:
            print "loop start:",node.m_data
            
            

def main_check_circular():
     l1 = gen_list([1,2,6,1,7])
     
     node6 = l1.m_next.m_next
     l1.append(node6)
     
     check_circular(l1)
    
    
        

"""
2.7 Implement a function to check if a linked list is a palindrome
"""
def gen_linked_list_from_list(plist):
    head = Node(plist[0])
    
    for e in plist[1:]:
        head.append(Node(e))

    return head
    
def is_polindrome(current, head):
    
    if current == None:
        return (head, True)
    
    (front, result) = is_polindrome(current.m_next, head)
    if (current.m_data == front.m_data):
        return (front.m_next, True and result)
    else:
        return (front.m_next, False and result)


def main_is_polindrome():
    head = gen_linked_list_from_list(list("abcdddcba"))
        
    print is_polindrome(head, head)
    


    
    


if __name__ == "__main__":
#     test_link_list()
#     main_remove_duplicate()
#     main_find_kth_last_element()
#     main_del_node()
#     main_partition()
#     main_sum_list()
    main_check_circular()
    main_is_polindrome()
    
    
    print "-----Done"