import math
from unittest.util import sorted_list_difference


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        runningSum = 0
        for i in range(k):
            runningSum += nums[i]
        biggestSum = runningSum
        for i in range(len(nums)  - k):
            runningSum = runningSum - nums[i] + nums[i + k]
            biggestSum = max(biggestSum,runningSum)
        return biggestSum / float(k)

print(Solution().findMaxAverage([5],1))



