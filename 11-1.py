class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map[key] if self.hash_map.get(key) is not None else -1

    def remove(self, key: int) -> None:
        if self.hash_map.get(key):
            self.hash_map.pop(key)

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(11, 0)
param_2 = obj.get(11)
print(param_2)
# obj.remove(key)