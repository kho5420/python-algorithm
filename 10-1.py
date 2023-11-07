from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.next, self.tail.next = self.tail, self.head
        self.head.prev, self.tail.prev = self.tail, self.head
        self.max_length = k
        self.length = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.length = self.length + 1

        node = ListNode(value, self.head.next, self.head)

        if self.length == 1:
            self.head.next = node
            self.tail.prev = node
        else:
            self.head.next.prev = node
            self.head.next = node

        """
        new node
        new.val = val
        new.next = head.next
        nex.prev = head
        head.next.prev = newnode
        """

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.length = self.length + 1

        node = ListNode(value, self.tail, self.tail.prev)

        if self.length == 1:
            self.tail.prev = node
            self.head.next = node
        else:
            self.tail.prev.next = node
            self.tail.prev = node

        """
        new node
        new.val = val
        new.next = tail
        nex.prev = tail.prev
        tail.prev.next = newnode
        """

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.length = self.length - 1

        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        """
        head 3 2 1 tail
        node
        head.next = head.next.next
        head.next.prev = head
        """
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.length = self.length - 1

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        """
        head 3 2 1 tail
        node
        tail.prev = tail.prev.prev
        tail.prev.next = head
        """

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.max_length

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(5)
param_1 = obj.insertFront(1)
param_11 = obj.insertFront(2)
param_12 = obj.insertFront(3)
param_2 = obj.insertLast(4)
param_21 = obj.insertLast(5)
param_22 = obj.insertLast(6)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
print(param_5)
param_6 = obj.getRear()
print(param_6)
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()