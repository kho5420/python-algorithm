# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next

        while current:
            print(current.val)
            current = current.next


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
Solution.oddEvenList(None, node)
