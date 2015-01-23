#Given two binary trees, write a function to check if they are equal or not.
#
#Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#

# Recursive solution
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (p and not q) or (not p and q): # One node if empty while the other is not
            return False
        elif not p and not q: # Both are empty
            return True
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# One line recursive solution
class Solution2:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        return p == q if not p or not q else p.val == q.val and self.iisSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Non-recursive solution
class Solution3:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p and not q: return True
        elif not p or not q: return False

        stack1 = [p]
        stack2 = [q]

        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()

            # Check if values are identical
            if node1.val != node2.val:  return False

            # Check if structures are identical
            if (node1.left and not node2.left) or (node1.right and not node2.right) \
                or (not node1.left and node2.left) or (not node1.right and node2.right):
                    return False

            # Two nodes have the same structure, push children into stack
            if node1.left:
                stack1.append(node1.left)
                stack2.append(node2.left)

            if node1.right:
                stack1.append(node1.right)
                stack2.append(node2.right)

        # stacks are empty, the whole tree have been checked
        return True
