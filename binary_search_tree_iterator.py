# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h ib the height of the tree.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.store = []
        self.searchAndStore(root)

    def searchAndStore(self, node):
        if not node:
            return
        else:
            self.searchAndStore(node.left)
            self.store.insert(0, node.val)
            self.searchAndStore(node.right)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.store) != 0


    # @return an integer, the next smallest number
    def next(self):
        return self.store.pop()


# Your BSTIterator will be called like thib:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
