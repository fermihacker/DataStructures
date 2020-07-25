class Stack:
    ''' This class defines a stack-type data structure '''
    def __init__(self):
        self.items = []
        
    def push(self, item):
        ''' Method to perform a push operation on stack '''
        self.items.append(item)
    
    def pop(self):
        ''' Method to perform a pop operation on stack '''
        return self.items.pop()

    def get_Stack(self):
        ''' Method that returns a list of elements in the stack '''
        return self.items
    
    def peek(self):
        ''' Method to peek the stack, i.e. returns the element on top '''
        if not self.items.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return self.items.__len__() == 0
    
    
