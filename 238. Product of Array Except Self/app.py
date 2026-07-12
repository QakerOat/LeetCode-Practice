class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def prefixProduct():
            newArr = []
            for elem in arr:
                if not newArr:
                    newArr.append(elem)
                else:
                    newArr.append(elem * newArr[-1])
            return newArr

        prefixProducts = prefixProduct(nums)
        nums.reverse
        reversePrefixProduct = prefixProduct(nums.reverse)
        reversePrefixProduct.reverse()
        nums.reverse

        return [(prefixProducts[i - 1] if i != 0 else 1) * (reversePrefixProduct[i + 1] if (i != len(nums) - 1) else 1) for i in range(len(nums))]


