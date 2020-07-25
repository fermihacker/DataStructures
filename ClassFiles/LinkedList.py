class Node:
    ''' This class creates a node object for the linked list '''
    def __init__(self, data = None):
        ''' The data in a node is None by default '''
        self.data = data
        self.next = None
    
    def __dtype__(self):
        ''' This method is to check the datatype of the element in node '''
        return type(self.data)

class LinkedList:
    ''' This class defines the main body of the linked list '''
    def __init__(self):
        ''' Initializes the head of the linked list '''
        self.head = None
       
    def printLis(self):
        ''' Method to print all elements in the linked list '''
        tempNode = self.head
        while tempNode.data != None:
            print(tempNode.data, end = ' ,')
            tempNode = tempNode.next
            if tempNode is None:
                break
    
    def appendOnHead(self, item):
        newNode = Node(item)
        newNode.next = newNode
        self.head = newNode
        
    def appendOnTail(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            return 
        
        elem = self.head
        
        while elem.next:
            elem = elem.next
        elem.next = newNode
    
    def midInsert(self, midNode, item):
        
        if midNode is None:
            raise "The Mentioned Node is not present"
            return 
        
        tempNode = Node(item)
        tempNode.next = midNode.next
        midNode.next = tempNode
    

        
