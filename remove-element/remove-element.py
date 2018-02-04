class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0

        while True:
            if i == len(nums):
                break
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)

A = Solution()

In = [3,2,2,3]
print A.removeElement(In,3) == 2
print In

In = [3,2,2,3]
print A.removeElement(In,5) == 4
print In