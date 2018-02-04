class Solution(object):

    def binarySearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int (Index)
        """

        if len(nums) == 0:
            return -1

        mid = len(nums) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            end = mid
            return self.binarySearch(nums[:end], target)
        else:
            start = mid + 1
            r = self.binarySearch(nums[start:], target)
            if r >= 0:
                return r + start
            else:
                return -1

    def binarySearchEdge(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int (Index)
        """

        if len(nums) == 0:
            return -1

        mid = len(nums) // 2

        if target == nums[mid]:
            start = mid + 1
            r = self.binarySearchEdge(nums[start:], target)
            if r >= 0:
                return r + start
            else:
                return mid
        else:
            end = mid
            return self.binarySearchEdge(nums[:end], target)


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = self.binarySearch(nums, target)

        if i < 0:
            return [-1, -1]

        else:
            lower = i - self.binarySearchEdge(nums[:i+1][::-1], target)
            upper = self.binarySearchEdge(nums[i:], target) + i
            return [lower, upper]




A = Solution()

print A.binarySearch([1,2,3,4], 1) == 0
print A.binarySearch([1,2,3,4], 4) == 3
print A.binarySearch([1,2,4], 1) == 0
print A.binarySearch([1,2,4], 4) == 2
print A.binarySearch([5, 7, 7, 8, 8, 10], 8) in range(3, 4)
print A.binarySearch([1, 1, 2, 3, 4, 5, 8, 9, 9, 9, 9, 10, 20, 50], 9) in range(7, 10)
print A.binarySearch([1,1,2,3,4,5,7,7,7,7,7,7,7,7,7,7,7,8,9,9], 9) in range(18,19)

print A.searchRange([1,3], 1) == [0,0]
print A.searchRange([1,2,3,3,3,3,4,5,9], 3) == [2,5]
print A.searchRange([5, 7, 7, 8, 8, 10], 8) == [3,4]
print A.searchRange([5, 7, 7, 8, 9, 10], 8) == [3,3]
print A.searchRange([1,1,2,3,4,5,8,9,9,9,9,10,20,50], 9) == [7, 10]
print A.searchRange([1,1,2,3,4,5,7,7,7,7,7,7,7,7,7,7,7,8,9,9,9,9,9,9,9], 9) == [18,24]
print A.searchRange([9,9,9,9,9,9,9], 9) == [0, 6]
print A.searchRange([1,2,3], 1) == [0,0]
print A.searchRange([1,2,3], 3) == [2,2]
print A.searchRange([1,1,2,3,10,20,50], 9) == [-1, -1]