# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSorter(pairs, 0,len(pairs)-1)

    
    def mergeSorter(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        mid = (start + end) //2

        self.mergeSorter(pairs, start, mid)
        self.mergeSorter(pairs, mid+1, end)

        self.merge(pairs, start, mid, end)

        return pairs

    
    def merge(self, pairs, start, mid, end):
        left = pairs[start:mid+1]
        right = pairs[mid+1:end+1]

        i, j, k = 0,0,start

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1

            else:
                pairs[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1

