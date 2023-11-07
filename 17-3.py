# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 147
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        sorted_head = ListNode()
        current = head

        while current:
            next_node = current.next
            prev = sorted_head

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current
            current = next_node

        return sorted_head.next

list_node = ListNode(4, ListNode(2, ListNode(1, ListNode(3, None))))
Solution().insertionSortList(list_node)