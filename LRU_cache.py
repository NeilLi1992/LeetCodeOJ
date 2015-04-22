#  Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Using linked list for implementation
# class LRUCache:
#     class Node:
#         def __init__(self, key, val):
#             self.key = key
#             self.val = val
#             self.next = None
#
#     # @param capacity, an integer
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.head = self.tail = None
#         self.dummy_head = Node(None, None)
#         self.dummy_head.next = self.head
#
#     # @return an integer
#     def get(self, key):
#         if not self.head:
#             # Cache is empty
#             return -1
#         else:
#             pre = self.dummy_head
#             cur = self.head
#             while cur:
#                 if cur.key == key:
#                     # Found
#                     value = cur.value
#
#                     # Get this Node to the end of list
#                     pre.next = cur.next
#                     if cur == self.head:
#                         self.head = cur.next
#                     self.tail.next = cur
#                     cur.next = None
#                     self.tail = cur
#
#                     return value
#                 else:
#                     pre = pre.next
#                     cur = cur.next
#             # Not found
#             return -1
#
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):
#         pre = self.dummy_head
#         cur = self.head
#         while cur:
#             if cur.key == key:
#                 # found
#                 cur.value = value
#
#                 # Get this Node to the end of list
#                 pre.next = cur.next
#                 if cur == self.head:
#
#             else:
#                 cur = cur.next
#
#         # Not fonud, insert
#         if self.size == self.capacity:
#             # delete the least recently used
#             pass
#         else:
#             #
#         pass

import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = collections.deque(maxlen=capacity)

    # @return an integer
    def get(self, key):
        for i in range(len(self.cache)):
            k,v = self.cache[i]
            if k == key:
                # found
                self.cache.remove((k,v))
                self.cache.append((k,v))
                return v
        else:
            # not found
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        for i in range(len(self.cache)):
            k,v = self.cache[i]
            if k == key:
                self.cache.remove((k,v))
                break

        self.cache.append((key, value))

L = LRUCache(3)
print
