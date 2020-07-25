from LinkedList import *
from collections import *

class Queue:
    
    ''' This class defines a queue data structure '''
    
    def __init__(self):
        ''' __init__ method initializing the queue '''
        self.queue = list()
    
    def enqueue(self, item):
        ''' Method to perform the enqueue operation on the queue '''
        if item != None:
            self.queue.insert(0, item)
        else:
            raise Exception
    
    def getSize(self):
        ''' This method returns the size of the queue '''
        return self.queue.__len__()
    
    def queuePop(self):
        ''' Method to perform the dequeue operation on the queue '''
        if self.queue.__len__() > 0:
            return self.queue.pop()
        else:
            raise "No elements in queue"
        
    def peek(self):
        ''' Method to perform a peek operation on the queue '''
        if self.queue.__len__() == 0:
            return -1
        return self.queue
    
    

    
    
        
        