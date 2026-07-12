class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        runningCount = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if s[i] in vowels:
                runningCount += 1
        currCount = runningCount
        for i in range(len(s) - k):
            if s[i] in vowels:
                runningCount -= 1
            if s[i + k] in vowels:
                runningCount += 1

            currCount = max(runningCount, currCount)
        return currCount

print(Solution().maxVowels("a", 1))