import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# TreeNode
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None # BinarySearchTree
        self.right = None # BinarySearchTree 

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        # if smaller, go left
        # if bigger, go right
        
        # if no node to go to  (i.e, left or right is None)
            # make the new node at that spot   
     if value < self.value:
       if not self.left:
        self.left = BinarySearchTree(value)
       else:
        self.left.insert(value)
     elif value >= self.value:
       if not self.right:
        self.right = BinarySearchTree(value)
       else:
        self.right.insert(value)   

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare value to the current node value
        # if smaller, go left 
        # if bigger, go right
        # if equal, return True!

        # if smaller, but we cant go left, return false
        # if bigger, but we cant go right, return false
      if self.value == target:
          return True
      elif self.value > target:
        if self.left is None:
          return False
        return self.left.contains(target)
      elif self.value < target:
        if self.right is None:
          return False
        return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
      # RECURSIVE SOLUTION
        if self.right is None:
           return self.value
        return self.right.get_max()

      # ITERATIVE SOLUTION
      # current_value = self
      # max_value = 0
      # while current_value:
      #   max_value = current_value.value
      #   current_value = current_value.right
      # return max_value
      

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
     cb(self.value)
     if self.left and self.left is not None:
        self.left.for_each(cb)
     if self.right and self.right is not None:
        self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
             # go left FIRST
        if node.left is not None:
            node.in_order_print(node.left)

        # print ourselves
        print(node.value)    

        # go right 
        if node.right is not None:
            node.in_order_print(node.right)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # use a queue
        # add current node to q
        # while q is not empty
        # add current node's children to q
        # pop current node
        node_queue = Queue()
        curNode = node
        node_queue.enqueue(curNode.value)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack()
        curNode = node

        while True:
            if curNode is not None:
                node_stack.push(curNode)
                curNode = curNode.left
            # if stack is not empty
            elif node_stack.len() > 0:
                curNode = node_stack.pop()
                print(curNode.value)
                curNode = curNode.right
            else:
                break

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
