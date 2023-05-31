# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node: # You are not allowed to modify this class
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        # create new node
        new_node = Node(value)

        # check if the list is empty
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        # check if the value is smaller than the head
        if value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        # check if the value is larger than the tail
        if value > self.tail.value:
            self.tail.next = new_node
            self.tail = new_node
            return

        # find the correct position to insert the new node
        current = self.head
        while current.next and current.next.value < value:
            current = current.next

        # insert the new node
        new_node.next = current.next
        current.next = new_node

        pass


    def split(self):
        #If the list is empty, return two empty lists
        if not self.head:
            return None, None
        #Initialize two pointers slow and fast to the first and second nodes in
        #the list
        slow = self.head
        fast = self.head.next
        #Use the slow and fast pointers to find the middle node in the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Create two new empty linked lists called sub1 and sub2
        sub1 = SortedLinkedList()
        sub2 = SortedLinkedList()
        sub2.head = slow.next
        sub2.tail = self.tail
        #Set the head and tail of sub1 to the beginning of the list to the middle
        #node
        sub1.head = self.head
        sub1.tail = slow
        slow.next = None
        #Return the two new sub-lists
        return sub1, sub2

        pass

 
    def removeDuplicates(self):
        # If the list is empty, return None
        if self.head is None:
            return None

        # Initialize two pointers, one to keep track of the current node, and another to keep track of the previous node.
        current = self.head
        prev = self.head

        # Traverse the list
        while current is not None:
            # If the current node's value is the previous node's value , it is a
            # duplicate.
            if current.value == prev.value:
                # Remove the current node by linking the previous node to the next node and skipping over the current node.
                prev.next = current.next
                current = current.next
            else:
                # Add the current node's value to the set and move the previous pointer to the current node.
                prev = current
                current = current.next
        pass

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(replace, globals(), name='LAB4',verbose=True)

if __name__ == "__main__":
    run_tests()
