class Solution(object):

    def nSum(self, nums, target, n):
        if n == 2:
            r = []
            d = {}
            for x in nums:
                d[target - x] = True
            for x in nums:
                if d.get(target - x):
                    d[target-x] == False
                    d[x] = False
                    r.append(set([x, target - x]))
            return r

        else:
            r = []
            for i in range(len(nums)):
                sublist = self.nSum(nums[:i] + nums[i + 1:], target - nums[i], n - 1)
                for l in sublist:
                    l.add(nums[i])
                    if l not in r:
                        r.append(l)
            return r

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSum(nums, target, 4)


A = Solution()

print A.fourSum([1, 0, -1, 0, -2, 2], 0)

#[
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#]