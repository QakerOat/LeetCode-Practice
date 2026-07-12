class Solution:
    def removeStars(self, s: str) -> str:
        myStack = []
        for elem in s:
            if elem == "*":
                myStack.pop()
            else:
                myStack.append()

        newString = "".join(myStack)
        return newString