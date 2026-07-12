class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        myStack = []
        for i in range(len(asteroids)):
            if len(myStack) < 1:
                myStack.append(asteroids[i])
            else:
                if asteroids[i] > asteroids[i - 1]:
                    continue
                if asteroids[i] < asteroids[i - 1]:


        return myStack



print(Solution().asteroidCollision([5,10,-5]))