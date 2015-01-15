# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.record = []

    def push(self, x):
        self.stack.append(x)
        if not self.record or x < self.record[-1][0]:
            self.record.append([x,1])
        else:
            for t in self.record:
                if x == t[0]:
                    t[1] += 1
                    break
        return x

    # @return nothing
    def pop(self):
        if self.stack:
            x = self.stack.pop()
            for i,t in enumerate(self.record):
                if x == t[0]:
                    t[1] -= 1
                    if t[1] == 0:
                        del self.record[i]


    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.record[-1][0]
