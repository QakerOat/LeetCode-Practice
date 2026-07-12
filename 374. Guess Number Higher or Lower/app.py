class Solution:

    def guess(self, num: int) -> int:
        pick = 2
        if pick == num:
            return 0
        if pick < num:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        leftNum = 1
        rightNum = n
        while leftNum <= rightNum:
            chooseNum = (leftNum + rightNum) // 2
            varGuess = self.guess(chooseNum)
            if varGuess == -1:
                rightNum = chooseNum - 1
            elif varGuess == 1:
                leftNum = chooseNum + 1
            else:
                return chooseNum


print(
    Solution().guessNumber(n = 2)
)