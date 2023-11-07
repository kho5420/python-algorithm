# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        3 4 2
        4 6 5
        -----
        8 0 7
        """

        """
        2   4   3 
        5   6   4
        ----------
        7  10   7
        """
        head = ListNode(0)
        current = head

        next_quotient = 0

        while True:
            if l1.val + l2.val + next_quotient < 10:
                current.next = ListNode(l1.val + l2.val + next_quotient)
                next_quotient = 0
            else:
                next_quotient, remainder = divmod(l1.val + l2.val + next_quotient, 10)
                current.next = ListNode(remainder)

            if not l1.next and not l2.next:
                if next_quotient > 0:
                    current = current.next
                    current.next = ListNode(next_quotient)
                break

            current = current.next

            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)

        while head:
            print(head.val)
            head = head.next

        # return head.next


# node = ListNode(2, ListNode(4, ListNode(3, None)))
# node2 = ListNode(5, ListNode(6, ListNode(4, None)))
# node = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
# node2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
node = ListNode(2, ListNode(4, ListNode(9, None)))
node2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9, None))))
Solution.addTwoNumbers(None, node, node2)
