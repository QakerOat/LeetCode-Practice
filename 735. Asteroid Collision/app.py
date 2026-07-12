class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        myStack = []
        for asteroid in asteroids:

            myStack.append(asteroid)
            while len(myStack) > 1:
                initialLengthofStack = len(myStack)
                topOfStack = myStack.pop()
                bottomOfStack = myStack.pop()

                if bottomOfStack > 0 and topOfStack < 0:
                    asteroidGoingLeft = abs(topOfStack)
                    asteroidGoingRight = bottomOfStack


                    if asteroidGoingLeft == asteroidGoingRight:
                        continue
                    elif asteroidGoingLeft < asteroidGoingRight:
                        myStack.append(asteroidGoingRight)
                    else:
                        myStack.append(topOfStack)
                else:
                    myStack.append(bottomOfStack)
                    myStack.append(topOfStack)
                    break



        return myStack



print(Solution().asteroidCollision([5,10,-5]))