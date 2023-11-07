# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []

        while True:
            lst.append(head.val)

            if head.next is None:
                break
            else:
                head = head.next

        print(lst)

        for i in range(0, len(lst)):
            if lst[i] == lst[len(lst) - i - 1]:
                continue
            else:
                return False

        return True

# node = ListNode(1, ListNode(2, None))
node = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
Solution.isPalindrome(None, node)
