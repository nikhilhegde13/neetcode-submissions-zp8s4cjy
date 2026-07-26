class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for rock in asteroids:
            while stack and rock < 0 and stack[-1] > 0:
                if abs(rock) > stack[-1]:
                    stack.pop()
                elif abs(rock) < stack[-1]:
                    rock = 0
                else:
                    rock = 0
                    stack.pop()  
            if rock:
                stack.append(rock)
        return stack
            