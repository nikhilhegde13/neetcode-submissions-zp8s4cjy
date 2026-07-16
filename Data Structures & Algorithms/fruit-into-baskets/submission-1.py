class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left, total, res = 0, 0, 0

        for right in range(len(fruits)):
            count[fruits[right]] += 1
            total += 1

            while len(count) > 2:
                total -= 1
                count[fruits[left]] -= 1
                if not count[fruits[left]] :
                    count.pop(fruits[left])
                left += 1
            
            res = max(res, total)
        
        return res