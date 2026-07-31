class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed = sorted((e, p, i) for i, (e, p) in enumerate(tasks))

        available = []
        order = []
        time = 0
        i = 0

        while len(order) < n:
            while i < n and indexed[i][0] <= time:
                _, p, idx = indexed[i]
                heapq.heappush(available, (p, idx))
                i += 1

            if not available:
                time = indexed[i][0]
                continue

            p, idx = heapq.heappop(available)
            time += p
            order.append(idx)

        return order
