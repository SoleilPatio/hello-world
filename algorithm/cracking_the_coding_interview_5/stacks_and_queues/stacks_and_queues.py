"""
3.1 Describe how you could use a single array to implement three stacks.
"""

"""
3.2 How would you design a stack which, in addition to push and pop, also has a
function min which returns the minimum element? Push, pop and min should
all operate in O(1) time.
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None
        pass
    
    def Push(self, data):
        new_node = Node(data)
        
        #1st
        if(self.head == None):
            self.head = new_node
        #other
        else:
            new_node.next = self.head
            self.head = new_node

    
    def Pop(self):
        if(self.head == None):
            return None
        
        pop_node = self.head
        self.head = self.head.next
        
        return pop_node.data
    
    def Peep(self):
        return self.head.data if self.head != None else None
    
    
    
    def ShowContent(self):
        head = self.head
        
        while(head != None):
            print head.data,"->",
            head=head.next
        print "Null"
        
    def ShowContent2(self):
        head = self.head
        print "\t\t:",
        while(head != None):
            print head.data.data,"->",
            head=head.next
        print "Null"
        
        

class MinStack(Stack):
    def __init__(self):
        super(MinStack,self).__init__()
        self.min_stack = Stack()

    
    def Push(self, data):
        super(MinStack,self).Push(data)
        
        new_node = self.head
        
        #1st
        if(self.min_stack.Peep() == None):
            self.min_stack.Push(new_node)
        #other
        else:
            if (new_node.data <= self.min()):
                self.min_stack.Push(new_node)
                
    
    def Pop(self):
        pop_node = self.head
        pop_data = super(MinStack,self).Pop()
        
        if pop_node == self.min_stack.Peep():
            self.min_stack.Pop()
            
        return pop_node.data if pop_node != None else None
    
        
    def min(self):
        return self.min_stack.Peep().data
        

def main_min_stak():
    import numpy as np
    
    stack = MinStack()
    
    for i in np.random.randint(10,size=10):
        stack.Push(i)
        stack.ShowContent()
        stack.min_stack.ShowContent2()
        
    while( stack.Pop() != None):
        stack.ShowContent()
        stack.min_stack.ShowContent2()
        
        
            
                
        
            
        

"""
3.3 Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack
exceeds some threshold. Implement a data structure SetOfStacks that mimics
this. SetOfStacks should be composed of several stacks and should create a
new stack once the previous one exceeds capacity. SetOfStacks.push() and
SetOfStacks.pop() should behave identically to a single stack (that is, pop()
should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on
a specific sub-stack.
"""
class CountingStack(Stack):
    def __init__(self):
        super(CountingStack, self).__init__()
        self.count = 0
    
    def Push(self, data):
        self.count += 1
        return super(CountingStack, self).Push(data) #Try Stack.Push(self, data): ==> multiple inheritance will has problem
    
    def Pop(self):
        if self.count > 0:
            self.count -= 1
        return super(CountingStack, self).Pop()
    
            
    
    
    
class SetOfStack(object):
    def __init__(self):
        self.current_stack = None
        self.stackofstack = CountingStack()
        self.threshold = 10
        
    def Push(self, data):
        if ( self.current_stack == None):
            self.current_stack = CountingStack()
        if ( self.current_stack.count >= self.threshold ):
            self.stackofstack.Push(self.current_stack)
            self.current_stack = CountingStack()
        
        self.current_stack.Push(data)
        
    def Pop(self):
        if ( self.current_stack == None):
            return None
        
        if (self.current_stack.count <= 0):
            while( True ):
                self.current_stack = self.stackofstack.Pop()
                if self.current_stack == None:
                    return None
                if self.current_stack.count > 0:
                    break
                
        return self.current_stack.Pop()
    
    # i:0-index
    def PopAt(self, i):
        total_count = self.stackofstack.count
        
        if (i > total_count):
            return None
        
        if i == total_count:
            return self.current_stack.Pop()
        else:
            count = total_count - i -1
            p_stack = self.stackofstack.head
            while(count > 0 and p_stack != None):
                p_stack = p_stack.next
                count -= 1
            if(p_stack != None):
                return p_stack.data.Pop()
        return None
                
                
                
                
        
        
        
    
    
    def ShowContent(self):
        
        print "-----"
        if( self.current_stack != None):
            self.current_stack.ShowContent()
        
        node = self.stackofstack.head
        while (node != None):
            node.data.ShowContent()
            node = node.next
            
        print "-----"
            
                
   
def main_StackOfStack():
    SOS = SetOfStack()
    for data in range(100):
        SOS.Push(data)
        
    SOS.ShowContent()
    
    for loop in range(10):
        for index in range(10):
            print SOS.PopAt(index),
        print ""
        
         
           
        
        
        
        
        
        

"""
3.4 In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom (i.e., each disk sits on top of an
even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks
"""

def hanoi_move(count, from_stack, middle_stack, to_stack, callback):
    
    if count == 1:
        data = from_stack.Pop()
        if data == None:
            return
        to_stack.Push(data)
        callback()
        
        return
    
    hanoi_move(count-1, from_stack, to_stack,middle_stack,callback)
    hanoi_move(1, from_stack, middle_stack,to_stack,callback)
    hanoi_move(count-1, middle_stack, from_stack,to_stack,callback)
 
 
A_stack = Stack()
B_stack = Stack()
C_stack = Stack()   
def callback():
    print "-------------------"
    A_stack.ShowContent()
    B_stack.ShowContent()
    C_stack.ShowContent()
    

def main_hanoi_move():
    for data in reversed(range(10)):
        A_stack.Push(data)
    A_stack.ShowContent()
    
    hanoi_move(10,A_stack, B_stack, C_stack,callback)


"""
3.5 Implement a MyQueue class which implements a queue using two stacks.
"""
class MyQueue(object):
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack = Stack()

    def _move_stack(self, from_s, to_s):
        while( True ):
            data = from_s.Pop()
            if data == None:
                break
            to_s.Push(data)
            
    def Push(self,data):
        self._move_stack(self.pop_stack, self.push_stack)
        self.push_stack.Push(data)
        
    def Pop(self):
        self._move_stack(self.push_stack, self.pop_stack)
        return self.pop_stack.Pop()
    
    
def main_MyQueue():
    mq = MyQueue()
    
    for data in range(10):
        mq.Push(data)
        
    while (True):
        data = mq.Pop()
        if data == None:
            break
        print data,
        
        
        
        
        

"""
3.6 Write a program to sort a stack in ascending order (with biggest items on top).
You may use at most one additional stack to hold items, but you may not copy
the elements into any other data structure (such as an array). The stack supports
the following operations: push, pop, peek, and isEmpty.
"""

def sort_stack_asc(in_stack):
    temp_stack = Stack()
    
    while (True):
        data = in_stack.Pop()
        if data == None:
            break
        
        sort_data = temp_stack.Peep()
        if(sort_data == None):
            temp_stack.Push(data)
            continue
        
        count = 0
        while( sort_data < data ):
            count += 1
            temp = temp_stack.Pop()
            in_stack.Push(temp)
            sort_data = temp_stack.Peep()
            if(sort_data == None):
                break
        
        temp_stack.Push(data)
        
        while( count > 0):
            count -= 1
            temp_stack.Push(in_stack.Pop())
    
    
       
    #copy back
    while (True):
        data = temp_stack.Pop()
        if data == None:
            return
        in_stack.Push(data)
        
def main_sort_stack_asc():
    import numpy as np
    
    mystack = Stack()
    
    for data in np.random.randint(10,size=10):
        mystack.Push(data)
        
    mystack.ShowContent()
    sort_stack_asc(mystack)
    mystack.ShowContent()
    

"""
3.7 An animal shelter holds only dogs and cats, and operates on a strictly "first in,
first out" basis. People must adopt either the "oldest" (based on arrival time) of
all animals at the shelter, or they can select whether they would prefer a dog or
a cat (and will receive the oldest animal of that type). They cannot select which
specific animal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog and
dequeueCat.You may use the built-in LinkedList data structure.
"""
class Queue(object):
    def __init__(self):
        self.queue = []
        
    def Push(self, data):
        self.queue.append(data)
        
    def Pop(self):
        if len(self.queue) == 0:
            return None
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def Peep(self):
        if len(self.queue) == 0:
            return None
        data = self.queue[0]
        return data
        
        
         


class AnimalRecord(object):
    def __init__(self, type):
        self.type = type
        self.no = None
    
        
class AnimalQueue(object):
    def __init__(self):
        self.serialno = 0
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        
    def Push(self, animal):
        self.serialno += 1
        animal.no = self.serialno
        
        if animal.type == "dog":
            self.dog_queue.Push(animal)
        elif animal.type == "cat":
            self.cat_queue.Push(animal)
            
    def DequeueAny(self):
        peep_dog = self.dog_queue.Peep()
        peep_cat = self.cat_queue.Peep()
        
        if peep_dog==None:
            return self.DequeueCat()
        elif peep_cat==None:
            return self.DequeueDog()
        
        
        if peep_dog.no > peep_cat.no:
            return self.DequeueCat()
        else:
            return self.DequeueDog()
            
    
    def DequeueDog(self):
        return self.dog_queue.Pop()
    
    def DequeueCat(self):
        return self.cat_queue.Pop()
    
    def ShowContent(self):
        print "DOG:",
        for r in self.dog_queue.queue:
            print "(%d,%s)"%(r.no,r.type),"<-",
        print ""
        
        print "CAT:",
        for r in self.cat_queue.queue:
            print "(%d,%s)"%(r.no,r.type),"<-",
        print ""
        
        
            
        

def main_animal_queue():
    import numpy as np
    aq = AnimalQueue()
    
    for animal in np.random.randint(2, size=10):
        animal_record = AnimalRecord("dog" if animal==0 else "cat")
        aq.Push(animal_record)
        
    aq.ShowContent()
    
    while True:
        ani = aq.DequeueAny()
        if ani == None:
            break
        print "---------------"
        print "(%d,%s)"%(ani.no, ani.type)
        aq.ShowContent()
        
    


if __name__ == "__main__":
#     main_min_stak()
#     main_StackOfStack()
#     main_hanoi_move()
#     main_MyQueue()
#     main_sort_stack_asc()
    main_animal_queue()
    
    print "Done!!"