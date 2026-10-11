import numpy as np

class DSAStack:
    def __init__(self, size=100):   # maximum size of stack is 100
        self.size = size    # size of stack
        self.count = 0  # count of elements entered in stack
        self.stack = np.empty(size, dtype = object) # empty stack of size either input by user or size 100

    def __str__(self):
        return (f"Stack: {self.stack}  Size: {self.size}")  # returns stack and its size

    def get_count(self):    # returns number of values in stack
        return self.count

    def isEmpty(self):  # returns 0 as it is empty
        return self.count == 0
    
    def isFull(self):   # returns self.count as it is full
        return self.count == len(self.stack)
            
        
    def push(self, val):    # insert a value
        if self.isFull():   # if full, an error message is displayed
            raise Exception("Stack is full")
        else:   # if not full, then value successfully inserted
            self.stack[self.count] = val        # value inserted at index
            self.count += 1     # increment count by 1

    def top(self):
        if self.isEmpty():      # if empty, an error message is displayed
            raise Exception("Stack is empty")
        else:
            top_val = self.stack[self.count - 1]    # value on top of stack assigned to top_val
            return top_val  # show value on top of stack
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            
            pop_val = self.stack[self.count-1]     # value on top of stack assigned to pop_val
            self.stack[self.count-1] = None
            self.count -= 1     # decrease count by 1
            return pop_val  # displays value on top to be removed

    def display_stack(self):    # displays the stack at its status quo
        
        return (f"Stack: {self.stack}")

class DSAQueue:
    def __init__(self, size=100):   # maximum size of queue is 100
        self.size = size    # size of queue
        self.count = 0  # count of elements entered in queue
        self.queue = np.empty(size, dtype=object)    # empty queue of size either input by user or size 100
        self.front = 0  # index of first value
        self.rear = -1 # index of latest value added at the back

    def __str__(self):
        return (f"Queue: {self.queue} Size of queue is {self.size}")    # returns queue and its size

    def get_count(self):    # returns number of values in queue
        return self.count
    
    def isEmpty(self):  # returns 0 as it is empty
        return self.count == 0  
    
    def isFull(self):   # returns self.count as it is full
        return self.count == len(self.queue)
    
            
    def enqueue(self, val): # insert a value
        if self.isFull():   # if full, an error message is displayed
            raise Exception("Queue is full")
        else:   # if not full, then value successfully inserted
            self.rear += 1     # increment rear by 1
            self.queue[self.rear] = val    # value inserted at rear
            self.count += 1     # increment count by 1

    def dequeue(self):
        if self.isEmpty():      # if empty, an error message is displayed
            raise Exception("Queue is empty")
        else:
            val = self.queue[self.front]
            for i in range(1, self.count):  # move all elements to the left one by one
                self.queue[i - 1] = self.queue[i]

            self.rear -= 1 # moves rear a step back
            self.count -= 1     # decrease count by 1

            return val  # returns value removed from queue
        
    def top(self):
        if self.isEmpty():      # if empty, an error message is displayed
            raise Exception("Queue is empty")
        else:
            top_val = self.queue[self.front]    # value in front of queue assigned to top_val
            return top_val  # show value on top of stack
        
    def display_queue(self):    # displays the queue
         return (f"{self.queue[self.front:self.rear+1]} ")
        