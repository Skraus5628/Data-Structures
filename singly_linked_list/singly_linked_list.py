

class Node: 
    def __init__(self, value, next=None):
        self.value = value
        self.next = next #Nxt node in the list


class LinkedList:
    def __init__(self):
        self.head: Node = None #Points to the first node in the list
        self.tail: Node = None  #Points to the last node in the list
        self.length = 0
    # append / add ==> add_to_tail
    
    def add_to_tail(self, value):
        #Check if there's a tail
        #If there is no tail (empty list)
        if not self.tail: #could also check length, check if tail = None
        # Create a new node
            new_tail = Node(value, None)
        # set self, head and self.tail 

        #set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail




    #remove

    def remove_head(self):
        #IF not head (empty list)
        if not self.head:
            return None

        #List with one element:
        if self.head == self.tail:
        # Set self head to current_head.next(Which is also None)
            current_head = self.head
            self.head = None
        #Set self.tail to none
            self.tail = None
            self.length -= 1 #( -= is same as self.length -1)
            return current_head.value
        #Decrement lengthy by 1

        #If head(general case):
        else: 
        #Set self, head to current_head.next
            current_head = self.head
            self.head = current_head.next
                #return current_head.value
            self.length = self.length -1
            return current_head.value



    def remove_tail(self):
        pass