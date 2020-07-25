class Node:
    
    ''' Class To create a node object for the linked list '''
    
    def __init__(self, item):
        ''' __init__ method to initialize the Node Object '''
        self.item = item
        self.next = None
        self.previous = None    
        

class d_LinkedList:
    
    ''' Class to create a doubly linked list '''
    
    def __init__(self):
        
        ''' __init__ method to initialize the head of the linked-list '''
        
        self.head = None
    
    def push(self, item):
        
        ''' Method to perform a push operation on the linked-list '''
        
        newNode = Node(item)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
    
    def __len__(self, node):
        
        ''' Method to get the number of elements in the linked list '''
        
        while node != None:
            counter += 1
            last = node
            node = node.next
        
        return counter
            
    def insert(self, item, prevNode):
        
        ''' Method to insert an element in the linked list '''
        
        if prevNode is None:
            return 
        
        newNode = Node(item)
        prevNode.next = newNode
        newNode.prev = prevNode
        
        if newNode.next is not None:
            newNode.next.prev = newNode
    
    def getLis(self, node):
        
        ''' Method to print out the list '''
        
        while node is not None:
            print(node.data, end = ' ')
            last = node
            node = node.next
    
    def append(self, item,):
        
        ''' Method to append an element/item in the linked list '''
        
        newNode = Node(item)
        newNode.next = None
        
        if self.head == None:
            newNode.prev, self.head = None, newNode
            
        last = self.head
         
        while last.next != None:
            last = last.next
            
        last.next = newNode
        newNode.prev = last
        return 
