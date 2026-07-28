class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for score in items:
            hashmap[score[0]].append(score[1])
        heap = []
        ans= []
        for key in sorted(hashmap.keys()):
            heap = hashmap[key]
            heapq.heapify(heap)
            while len(heap) > 5:
                heapq.heappop(heap)
            
            ans.append([key, sum(heap)//5])
        
        return ans