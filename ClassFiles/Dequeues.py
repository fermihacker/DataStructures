class dequeue:
    
    ''' This class initializes a Double-sided Queue '''
    
    def __init__(self):
        ''' __init__ method to define the dequeue structure '''
        self.queue = []
        
    def __len__(self):
        ''' Method to get size of dequeue '''
        return len(self.queue)
    
    def addFront(self, item):
        ''' Method to add an item/element in front-position of the dequeue '''
        self.queue.append(item)
    
    def addRear(self, item):
        ''' Method to add an item/element in the rear-position of the dequeue '''
        self.queue.insert(0, item)
        
    def removeFront(self):
        ''' Method to remove an item/element in the front-position of the dequeue '''
        return self.queue.pop()
    
    def removeRare(self):
        ''' Method to remove an item/element in the rear-position of the dequeue '''
        return self.queue.pop(0)