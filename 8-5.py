# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
Solution.swapPairs(None, node)
