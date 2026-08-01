class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        ans = ""
        for count, c in [(-a, "a"), (-b,"b"), (-c,"c")]:
            if count != 0:
                heapq.heappush(heap, (count,c))
        
        while heap:
            count, curr = heapq.heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == curr:
                if not heap:
                    break
                cnxt, nxt = heapq.heappop(heap)
                ans += nxt 
                cnxt += 1
                if cnxt:
                    heapq.heappush(heap,(cnxt,nxt))
                heapq.heappush(heap,(count, curr))
            else:
                ans += curr
                count += 1
                if count:
                    heapq.heappush(heap,(count,curr))

        
        return ans

