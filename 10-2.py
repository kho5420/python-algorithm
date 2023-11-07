from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merge_list = []
        for node in lists:
            while node:
                merge_list.append(node.val)
                node = node.next

        if not merge_list:
            return None

        merge_list.sort()
        head = ListNode(merge_list[0], None)
        cur = head
        for i in range(1, len(merge_list)):
            cur.next = ListNode(merge_list[i])
            cur = cur.next

        return head

lst = [
    ListNode(1, ListNode(4, ListNode(5, None))),
    ListNode(1, ListNode(3, ListNode(4, None))),
    ListNode(2, ListNode(6, None))
]

Solution.mergeKLists(None, lst)