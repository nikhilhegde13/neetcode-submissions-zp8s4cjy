class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-cnt, c] for c, cnt in count.items()]
        heapq.heapify(heap)
        prev = None
        ans = ""
        while heap or prev:
            if prev and not heap:
                return ""
            count, c = heapq.heappop(heap)
            ans += c
            count += 1

            if prev:
                heapq.heappush(heap,prev)
                prev = None
            
            if count != 0:
                prev = [count, c]
            
        return ans
