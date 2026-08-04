class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        curr = 0
        for pas, start, end in trips:
            while heap and heap[0][0] <= start:
                curr -= heapq.heappop(heap)[1]
            
            curr += pas
            if curr > capacity:
                return False

            heapq.heappush(heap, [end, pas])

        
        return True