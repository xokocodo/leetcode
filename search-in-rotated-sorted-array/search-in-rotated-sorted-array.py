class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1


        mid = len(nums) // 2

        end = mid
        start = mid + 1

        if nums[mid] == target:
            return mid

        a = self.search(nums[:end], target)
        b = self.search(nums[start:], target)

        if b >= 0:
            b = b + start

        if a > -1:
            return a
        else:
            return b



A = Solution()

print A.search([1,2,3,4,5,6,7], 1) == 0
print A.search([4,5,6,7,1,2,3], 1) == 4
print A.search([4,5,6,7,8,9,10,11,12,13,14,15,1,2,3], 1) == 12
print A.search([4,5,6,7,8,9,10,11,1,2,3], 1) == 8
print A.search([4,5,6,7,8,9,10,1], 1) == 7
print A.search([4,5,6,7,8,9,10,1], 4) == 0
print A.search([4,5,6,7,1], 9) == -1
print A.search([0,1,2,3], 9) == -1
print A.search([0], 9) == -1
print A.search([], 9) == -1
