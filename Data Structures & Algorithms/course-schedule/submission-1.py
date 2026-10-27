class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = { i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            req[course].append(pre)

        curr = set()

        def dfs(sub):
            if sub in curr:
                return False
            
            if req[sub] == []:
                return True
            
            curr.add(sub)
            for pre in req[sub]:
                if not dfs(pre):
                    return False
            
            curr.remove(sub)
            req[sub] = []
            return True 

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True