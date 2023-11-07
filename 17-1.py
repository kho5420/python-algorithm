# Definition for singly-linked list.
from typing import Optional

# 148

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        node_list = []

        while True:
            node_list.append(head.val)

            if head.next is None:
                break
            else:
                head = head.next

        node_list.sort()
        root = ListNode(0, None)
        cur = root

        for val in node_list:
            cur.next = ListNode(val, None)
            cur = cur.next

        return root.next

list_node = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
Solution().sortList(list_node)