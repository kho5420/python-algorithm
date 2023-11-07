# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []

        while head:
            print(head.val)
            lst.append(head.val)
            head = head.next

        lst.reverse()

        if not lst:
            return None

        head = ListNode(lst[0])
        current = head

        for i in range(1, len(lst)):
            new_node = ListNode(lst[i])
            current.next = new_node
            current = new_node

        return head


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
Solution.reverseList(None, node)
