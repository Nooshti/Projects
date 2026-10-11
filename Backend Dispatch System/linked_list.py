class DSAListNode:  # used inside linked list
    def __init__(self, inValue):
        self.value = inValue
        self.next = None
        self.prev = None
    def __str__(self):
        return f"{self.value}"
    
    def getValue(self):
        return self.value   # returns value in node
    
    def setValue(self, inValue):
        self.value = inValue    # sets value inside node

    def getNext(self):
        return self.next    # gets next value inside node
    
    def getPrev(self):
        return self.prev    # gets previous value inside node
    
    def setNext(self, newNext):
        self.next = newNext     # sets value inside of next node

    def setPrev(self, newPrev):
        self.prev = newPrev     # sets value inside of previous node

class DSALinkedList:
    def __init__(self):
        self.head = None    # sets self.head to None
        self.tail = None    # sets self.tail to None
        self.count = 0

    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)   # creates a new node with a given value in linked list
        if self.isEmpty():
            self.head = newNd   # if linked list is empty, then node is head
            self.tail = newNd   # node is also tail
            self.count += 1 # increment the num of elements in the linked list
        else:
            newNd.setNext(self.head)    # if not empty, point new node to current head
            self.head.setPrev(newNd)  # the previous node to self.head is new node
            self.head = newNd   # make new node the new head
            self.count += 1 # increment the num of elements in the linked list

    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd   # new node becomes the head
            self.tail = newNd   # new node becomes the tail
            self.count += 1 # increment the num of elements in the linked list
        else:
            
            newNd.setPrev(self.tail)
            self.tail.setNext(newNd)
            self.tail = newNd
            self.count += 1 # increment num of elements in list by 1

    def isEmpty(self):
        return self.head is None   # return True if head is None
            
        
    def peekFirst(self):
        if self.isEmpty():
            raise Exception("List is Empty")    # Abort with error
        else:
            nodeValue = self.head.getValue()
            return nodeValue    # return value of head node
    
    def peekLast(self):
        if self.isEmpty():
            raise Exception("List is Empty")    # Abort with error
        else:
            nodeValue = self.tail.getValue()   # value of last node
        return nodeValue

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is Empty")    # Abort with error
        else:
            nodeValue = self.head.getValue()    # store value of head node
            self.head = self.head.getNext() # move head to next node
            if self.head is not None:   
                self.head.setPrev(None)
            else:
                self.tail = None
            self.count -= 1 # decrease num of elements in list
        
        return nodeValue    # return removed value
    
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is Empty")    # Abort with error
        elif (self.head.getNext() is None) or (self.head == self.tail):   # if only 1 node exists
            nodeValue = self.tail.getValue()    # store its value
            self.head = None    # set head to None (list becomes empty)
            self.tail = None
            self.count -= 1
        else:   # multiple nodes
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
            self.count -= 1

        return nodeValue    

    def remove(self, value):    # removes any value by first traversing the linked list to find it
        run = 0
        if self.isEmpty():
            return None
        current_node = self.head
        while (run == 0 and current_node is not None):
            if current_node.getValue() == value:
                if current_node == self.head:
                    self.removeFirst()
                elif current_node == self.tail:
                    self.removeLast()
                else:
                    prev_node = current_node.getPrev()
                    next_node = current_node.getNext()
                    prev_node.setNext(next_node)
                    next_node.setPrev(prev_node)
                    self.count -= 1
                    run = 1
            current_node = current_node.getNext()


    def get_count(self):
        return self.count
    
    def display(self):
        currNd = self.head
        while currNd is not None:
            if currNd.getPrev() is None:
                print("Head <--> ", end = "")

            print(currNd.getValue(), end=" <--> ")
            currNd = currNd.getNext()
        print("Tail")