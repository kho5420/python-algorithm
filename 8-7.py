# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        index = 1

        current = head
        reverse_head = None
        reverse_val = None
        right_node = None

        while current:
            if left <= index <= right:
                if not reverse_head:
                    reverse_head = current
                    reverse_val = current
                else:
                    reverse_val.next = current
                    reverse_val = current
            elif right < index:
                right_node = current

            current = current.next
            index = index + 1

        if index == 2:
            return head
        elif index == 3:
            return reverseList(reverse_head)

        if reverse_val:
            reverse_val.next = None

        reverse_head = reverseList(reverse_head)

        index = 1
        current = head

        while current:
            if (left > 1 and index == left - 1) or (left == index):
                current.next = reverse_head
                left = 0
            elif index == right:
                current.next = right_node
                right = 0

            current = current.next
            index = index + 1

        while head:
            print(head.val)
            head = head.next


def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


# node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
node = ListNode(3, ListNode(5, None))
# node = ListNode(5, None)
Solution.reverseBetween(None, node, 1, 1)
