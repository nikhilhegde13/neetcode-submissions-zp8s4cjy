class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for s,d,w in times:
            adj[s].append((d,w))
        
        delay = 0
        heap = [(0,k)]
        visited = set()
        print(adj)
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            delay = weight

            for c,w in adj[node]:
                heapq.heappush(heap, (weight+w, c))
        
        return delay if len(visited) == n else -1