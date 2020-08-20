"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)
        #return self.size
        #len(self.storage) cleaner vers of doing self.size=len(self.storage) 
        #on each line at the end of push/pop
    def push(self, value):
        self.storage.append(value)
        #self.size = len(self.storage)
    def pop(self):
        if len(self) > 0:
            return self.storage.pop()
            #self.size = len(self.storage)
        else:
            return None
