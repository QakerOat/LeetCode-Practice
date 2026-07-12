class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPointer = 0
        rightPointer = len(nums) - 1
        testPointer = 0
        while leftPointer < rightPointer:
            testPointer = (leftPointer + rightPointer) // 2
            if nums[testPointer] < target:
                leftPointer = testPointer + 1
            elif nums[testPointer] > target:
                rightPointer = testPointer - 1
            else:
                return testPointer

        if nums[rightPointer] == target:
            return rightPointer
        elif rightPointer < leftPointer:
            return -1
        else:
            return -1

print(Solution().search(nums = [2,5], target = 0))