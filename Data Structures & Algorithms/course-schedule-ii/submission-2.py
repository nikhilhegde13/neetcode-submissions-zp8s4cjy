class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = { i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            req[course].append(pre)

        curr = set()
        visit = set()
        order = []

        def dfs(sub):
            if sub in curr:
                return False
            if sub in visit: 
                return True
            
            curr.add(sub)
            for pre in req[sub]:
                if not dfs(pre):
                    return False
            
            curr.remove(sub)
            visit.add(sub)
            order.append(sub)
            return True 

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order