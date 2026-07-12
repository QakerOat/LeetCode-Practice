from unittest.util import sorted_list_difference


class Solution(object):
    def majorityElement(self, nums):
        myDict = {}
        for elem in nums:
            if elem in myDict:
                myDict[elem] += 1
            else:
                myDict[elem] = 1

            if myDict[elem] >= len(nums) / 2:
                return elem

print(Solution().majorityElement(nums = [2,2,1,1,1,2,2]))