# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> my_tree = BinarySearchTree() 
        >>> my_tree.isEmpty()
        True
        >>> my_tree.insert(9) 
        >>> my_tree.insert(5) 
        >>> my_tree.insert(14) 
        >>> my_tree.insert(4)  
        >>> my_tree.insert(6) 
        >>> my_tree.insert(5.5) 
        >>> my_tree.insert(7)   
        >>> my_tree.insert(25) 
        >>> my_tree.insert(23) 
        >>> my_tree.getMin
        4
        >>> my_tree.getMax
        25
        >>> 67 in my_tree
        False
        >>> 5.5 in my_tree
        True
        >>> my_tree.isEmpty()
        False
        >>> my_tree.getHeight(my_tree.root)   # Height of the tree
        3
        >>> my_tree.getHeight(my_tree.root.left.right)
        1
        >>> my_tree.getHeight(my_tree.root.right)
        2
        >>> my_tree.getHeight(my_tree.root.right.right)
        1
        >>> my_tree.get_closest(18) 
        14
        >>> my_tree.get_closest(19) 
        23
        >>> my_tree.get_closest(5)  
        5
        >>> my_tree.get_closest(72) 
        25
        >>> my_tree.get_closest(7)  
        7
        >>> my_tree.get_closest(8) 
        9
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        'If there is not an initial node then the tree has to be empty'
        return self.root is None

        pass



    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        'Return the minimum value in the tree'
        
        if self.root is None:
            return None
        node = self.root
        '''

        Keep traversing through the left path of the tree because
        the values descend when going towards the left

        '''
        
        while node.left is not None:
            node = node.left
        return node.value

        pass



    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        'Return the maximum value in the tree'
        
        if self.root is None:
            return None
        
        node = self.root

        '''
        Keep traversing through the right path of the tree because
        the values ascend when going towards the right

        '''

        while node.right is not None:
            node = node.right
        return node.value

        pass



    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        return self.helper_contains(self.root, value)

        pass

    #helper function for __contain__
    def helper_contains(self, node, value):
        if node is None:
            return False
        #Return true if function is found in the tree
        elif value == node.value:
            return True

        '''
        Search to the left if the value is less than the current node being
        evaluated

        '''
        
        elif value < node.value:
            return self.helper_contains(node.left, value)
        '''
        Search to the right if the value is more than the current node being
        evaluated

        '''
        else:
            return self.helper_contains(node.right, value)



    def getHeight(self, node):
        # YOUR CODE STARTS HERE

        # Return the height of the tree/subtree rooted at the given node
        if node is None:
            return -1

        '''
        Repeat the function until you get none as a function meaning you've
        the bottom of the tree

        '''
        
        left_height = self.getHeight(node.left)
        right_height = self.getHeight(node.right)

        return max(left_height, right_height) + 1

        pass



    def get_closest(self, item):
        # YOUR CODE STARTS HERE

        # Return the value in the tree closest to the given item
        closest = None
        node = self.root
        while node is not None:
            #Return the value if it is in the tree
            if node.value == item:
                return node.value

            #Return value of the closest distance to the given item
            if closest is None or abs(node.value - item) < abs(closest - item):
                closest = node.value

            if node.value > item:
                node = node.left

            else:
                node = node.right

        return closest

        pass


def run_tests():
    import doctest

    #- Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    #doctest.run_docstring_examples(Calculator._getPostfix, globals(), name='HW3',verbose=True)   

if __name__ == "__main__":
    run_tests()



