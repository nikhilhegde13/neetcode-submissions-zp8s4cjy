class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []        

    def addNum(self, num: int) -> None:
        if self.heap2 and num < self.heap2[0]:
            heapq.heappush(self.heap1, -1*num)
        else:
            heapq.heappush(self.heap2, num)

        if len(self.heap1) > len(self.heap2)+1:
            transfer = -1 * heapq.heappop(self.heap1)
            heapq.heappush(self.heap2, transfer)
        if len(self.heap2) > len(self.heap1)+1:
            transfer = -1 * heapq.heappop(self.heap2)
            heapq.heappush(self.heap1, transfer)
    def findMedian(self) -> float:
        if len(self.heap1) > len(self.heap2):
            return -1 * self.heap1[0]
        elif len(self.heap1) < len(self.heap2):
            return self.heap2[0]
        else:
            return (self.heap2[0] + -1 *self.heap1[0]) / 2.0
        