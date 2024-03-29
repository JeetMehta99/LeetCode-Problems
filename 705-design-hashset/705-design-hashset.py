class MyHashSet:

    def __init__(self):
        self.array = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        subkey = key % 1000
        if not self.contains(key):
            self.array[subkey].append(key)

    def remove(self, key: int) -> None:
        subkey = key % 1000
        if self.contains(key):
            self.array[subkey].remove(key)

    def contains(self, key: int) -> bool:
        subkey = key % 1000
        return key in self.array[subkey]
    
    
    
    
###############################################

# Brute Force

# class MyHashSet:

#     def __init__(self):
#         self.array = [None for _ in range(1000000)]

#     def add(self, key: int) -> None:
#         if not self.contains(key):
#             self.array[key] = True

#     def remove(self, key: int) -> None:
#         if self.contains(key):
#             self.array[key] = None

#     def contains(self, key: int) -> bool:
#         return self.array[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)