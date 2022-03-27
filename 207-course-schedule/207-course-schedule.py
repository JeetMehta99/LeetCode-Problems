class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap for preReq courses
        preMap = { i:[] for i in range(numCourses)}
        # print(preMap)
        for cors, pre in prerequisites:
            preMap[cors].append(pre)

        visited = set()
        def dfs(cors):
            if cors in visited:
                return False
            if preMap[cors] == []:
                return True
            visited.add(cors)
            print(visited)
            for pre in preMap[cors]:
                if not dfs(pre):
                    return False
            visited.remove(cors)
            preMap[cors] = []
            return True
        
        for cors in range(numCourses):
            if not dfs(cors):
                return False
        return True
            
    
        
        
        
        