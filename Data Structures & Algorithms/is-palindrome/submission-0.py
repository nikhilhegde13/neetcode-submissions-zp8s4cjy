class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(new)
        first = 0
        last = len(new)-1

        while first < last:
            print(new[first])
            print(new[last])
            if new[first] == new[last]:
                first += 1
                last -= 1
            else:
                return False
        
        return True