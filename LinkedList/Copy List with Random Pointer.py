"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hash_table = {}

        ptr = head

        while ptr:
            if ptr.random is None:
                hash_table[ptr] = -1
            else:
                hash_table[ptr] = ptr.random.val
            ptr = ptr.next

        headNew = ptr = None

        random_hash = {}

        for keys in hash_table.keys():

            if headNew is None:
                headNew = Node(keys.val)
                random_hash[hash_table[keys]] = headNew
                ptr = headNew
            else:
                ptr.next = Node(keys.val)
                random_hash[hash_table[keys]] = ptr
                ptr = ptr.next

        ptr = head
        ptr1 = headNew

        while ptr:
            if ptr.random is None:
                ptr1.random = None
            else:
                item = random_hash[ptr.random.val]
                ptr1.random = item

            ptr = ptr.next
            ptr1 = ptr1.next

        return headNew