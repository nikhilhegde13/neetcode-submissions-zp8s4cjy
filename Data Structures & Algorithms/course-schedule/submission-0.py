class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            req[b].append(a)
        
        visited = set()

        def check(sub):
            if sub in visited:
                return False
            
            if req[sub] == []:
                return True

            visited.add(sub)
            for c in req[sub]:
                if not check(c):
                    return False
            
            visited.remove(sub)
            req[sub] = []

            return True

        for c in range(numCourses):
            if not check(c):
                return False
        
        return True 