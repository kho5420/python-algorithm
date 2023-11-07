class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue.pop(0)
            return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[0]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[len(self.queue) - 1]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return self.length == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()