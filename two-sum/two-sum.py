class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        remainders = {}

        for i in range(len(nums)):
            r = remainders.get(nums[i])
            if r != None:
                return [r, i]
            else:
                remainders[target-nums[i]] = i

        return None

A = Solution()

print A.twoSum([1,2], 3) == [0, 1]
print A.twoSum([2, 7, 11, 15], 9) == [0, 1]
print A.twoSum([90, 9, 900, 9000], 909) == [1, 2]