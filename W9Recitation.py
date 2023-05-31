def kth_smallest_1(self, k):
    if self.root is None:
        return None
    else:
        node_lst = self.inorder()
        if len(node_lst) >= k:
            return node_lst[k-1]



def kth_smallest_2(self, k):
    self.counter = 0
    return self._kth_helper(self.root, k)



def _kth_helper(self, node, k):
    if node is None or self.counter >= k:
        return None

    left = self._kth_helper(node.left, k)
    if left is not None:
        return left

    self.counter += 1
    if self.counter == k:
        return node.value

    return self._kth_helper(node.right, k)
