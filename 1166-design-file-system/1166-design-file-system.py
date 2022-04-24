class FileSystem:
    # HashMap
    def __init__(self):
        self.map = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.map: 
            return False
        parent = path[:path.rfind("/")]
        if parent and parent not in self.map: 
            return False
        self.map[path] = value
        return True 

    def get(self, path: str) -> int:
        return self.map.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)