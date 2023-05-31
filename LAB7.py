# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MaxBinaryHeap:
    '''
        >>> h = MaxBinaryHeap()
        >>> h.getMax
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [10, 5]
        >>> h.insert(14)
        >>> h._heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(14)
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> h.insert(20)
        >>> h
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.insert(20)
        >>> h
        [20, 20, 14, 14, 2, 10, 11, 5, 9]
        >>> h.getMax
        20
        >>> h._leftChild(1)
        20
        >>> h._rightChild(1)
        14
        >>> h._parent(1)
        >>> h._parent(6)
        14
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMax()
        20
        >>> h._heap
        [20, 14, 14, 9, 2, 10, 11, 5]
        >>> h.deleteMax()
        20
        >>> h
        [14, 9, 14, 5, 2, 10, 11]
        >>> len(h)
        7
        >>> h.getMax
        14
    '''

    def __init__(self):
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMax(self):
        # YOUR CODE STARTS HERE
        if len(self._heap) == 0:
            return None
        return self._heap[0]

        pass
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        if index <= 0 or index >= len(self):
            return None
        return (index - 1) // 2

        pass
        

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        leftIndex = 2 * index + 1
        if leftIndex >= len(self):
            return None
        return self._heap[leftIndex]

        pass


    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        rightIndex = 2 * index + 2
        if rightIndex >= len(self):
            return None
        return self._heap[rightIndex]


        pass
         

    def insert(self,x):
        # YOUR CODE STARTS HERE
        self._heap.append(x)
        self._percolateUp(len(self) - 1)


        pass

    def deleteMax(self):
        if len(self)==0:
            return None        
        elif len(self)==1:
            removed=self._heap[0]
            self._heap=[]
            return removed 

        # YOUR CODE STARTS HERE
        else:
            removed=self._heap[0]
            self._heap[0]=self._heap.pop()
            self._bubbleDown(0)
            return removed

        pass


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [9, 8, 7, 7, 4, 4, 2, 1, 1, 0, 0, -1]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [8, 5, 4, 3.1, 2, 1, 0, -15, -15, -15]
    '''
    # YOUR CODE STARTS HERE
    # Step 1: Build a max heap
    n = len(numList)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numList, n, i)
    
    # Step 2: Extract elements one by one from the max heap
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum value) with the last element
        numList[0], numList[i] = numList[i], numList[0]
        
        # Call heapify on the reduced heap to maintain the max heap property
        heapify(numList, i, 0)
        
    return numList



def heapify(numList, n, i):

        '''
    Helper function to maintain the max heap property
    
    numList: List[int/float] - the input list
    n: int - the size of the heap
    i: int - the index of the node to heapify
    '''
    largest = i # Initialize largest as root
    left = 2 * i + 1 # left = 2*i + 1
    right = 2 * i + 2 # right = 2*i + 2
    
    # If left child is larger than root
    if left < n and numList[left] > numList[largest]:
        largest = left
    
    # If right child is larger than largest so far
    if right < n and numList[right] > numList[largest]:
        largest = right
    
    # If largest is not root
    if largest != i:
        numList[i], numList[largest] = numList[largest], numList[i] # swap
        
        # Recursively heapify the affected sub-tree
        heapify(numList, n, largest)

    pass



# ============== EXTRA CREDIT
class PriorityQueue:
    '''
        >>> priority_q = PriorityQueue()
        >>> priority_q.isEmpty()
        True
        >>> priority_q.peek()
        >>> priority_q.enqueue('sara',0)
        >>> priority_q
        [(0, 'sara')]
        >>> priority_q.enqueue('kyle',3)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara')]
        >>> priority_q.enqueue('harsh',1)
        >>> priority_q
        [(3, 'kyle'), (0, 'sara'), (1, 'harsh')]
        >>> priority_q.enqueue('ajay',5)
        >>> priority_q
        [(5, 'ajay'), (3, 'kyle'), (1, 'harsh'), (0, 'sara')]
        >>> priority_q.enqueue('daniel',4)
        >>> priority_q.isEmpty()
        False
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.enqueue('ryan',7)
        >>> priority_q
        [(7, 'ryan'), (4, 'daniel'), (5, 'ajay'), (0, 'sara'), (3, 'kyle'), (1, 'harsh')]
        >>> priority_q.dequeue()
        'ryan'
        >>> priority_q.peek()
        'ajay'
        >>> priority_q
        [(5, 'ajay'), (4, 'daniel'), (1, 'harsh'), (0, 'sara'), (3, 'kyle')]
        >>> priority_q.dequeue()
        'ajay'
        >>> len(priority_q)
        4
        >>> priority_q.dequeue()
        'daniel'
        >>> priority_q.dequeue()
        'kyle'
        >>> priority_q.dequeue()
        'harsh'
        >>> priority_q.dequeue()
        'sara'
        >>> priority_q.dequeue()
        >>> priority_q.isEmpty()
        True
    '''

    def __init__(self):
        self._items = MaxBinaryHeap()

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    __repr__ = __str__

    def peek(self):
        # YOUR CODE STARTS HERE
        if len(heap) == 0:
            return None
        return heap[0]

        pass

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        """
        Returns True if the heap is empty, else False.
        """
        return len(self.heapList) == 0

        pass
    
    def enqueue(self, value, priority):
        # YOUR CODE STARTS HERE
        self.heap.append((value, priority))
        self._bubble_up(len(self.heap) - 1)

        pass
    
    def dequeue(self):
        # YOUR CODE STARTS HERE
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        value, priority = self.heap.pop()
        self._bubble_down(0)
        return value

        pass
    




