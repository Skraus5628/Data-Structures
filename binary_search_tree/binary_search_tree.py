"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare target value to node.value
        # if value > node.value:
        if value > self.value:
            # Go right
            # If node.right is None:
            if self.right is None:
                # Create the new node 
                self.right = BSTNode(value)
            else:
                # Do the same thing
                #Insert value into node.right
                #right_child is a BST node so we can call insert on it
                right_child = self.right
                right_child.insert(value)
        # Else if value < node.value
        if value < self.value:
            #go left
            #if node.left is None:
            if self.left is None:
                #create node
                self.left = BSTNode(value)
        else:
            #do the same thing
            # (compare, go left or right
            # insert value into node.left)
            left_child = self.left
            left_child.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #if the value matches the target - return true
        if self.value == target:
            return True 
        # if the value is left than the target check the value to the right

        elif self.value < target:
            #if there is no self.right/target not there return false
            if not self.right:
                return False
            #otherwise return that the right node contains the target
            else:
                return self.right.contains(target)
            #if the value is greater than the target check left
        elif self.value > target:
            if not self.left:
                return False
            else: return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right or self.left:
            if not self.right:
                return
            else:
                self.right.for_each(fn)
            if not self.left:
                return 
            else: self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node = None):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node = None):
        queue = Queue()
        if node: 
            queue.enqueue(node)
        else: queue.enqueue(self)

        while len(queue) > 0:
            current_node = queue.dequeue()

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            

            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
