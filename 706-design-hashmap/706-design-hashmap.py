class MyHashMap:
### BAD APPROACH
    def __init__(self):
        self.lis = [-1 for _ in range(1000001)]

    def put(self, key: int, value: int) -> None:
        self.lis[key] = value

    def get(self, key: int) -> int:
        return self.lis[key]

    def remove(self, key: int) -> None:
        self.lis[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)