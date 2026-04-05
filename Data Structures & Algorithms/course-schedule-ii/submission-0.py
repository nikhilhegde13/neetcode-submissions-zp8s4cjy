class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = { i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            reqs[a].append(b)

        sequence = []
        visited = set()
        cycle = set()
        def scheduler(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for c in reqs[course]:
                if not scheduler(c): return False

            cycle.remove(course)
            visited.add(course)
            sequence.append(course)
            return True
            
        for course in range(numCourses):
            if not scheduler(course) :
                return []
        
        return sequence