class Solution(object):

    def __init__(self):
        self.answers = [1, 1, 2, 5] + [0 for x in range(9996)]
        self.sumAtN = [1, 2, 4, 9] + [0 for x in range(9996)]
        self.solvedTo = 4

    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """

        for i in range(self.solvedTo, N+1):
            self.answers[i] = self.answers[i-1] + self.answers[i-2] + 2 * self.sumAtN[i-3]
            self.sumAtN[i] = self.sumAtN[i-1] + self.answers[i]
            self.solvedTo += 1

        return self.answers[N] % (10**9 + 7)


A = Solution()

print A.numTilings(3)
print A.numTilings(4)
print A.numTilings(5)
print A.numTilings(6)
print A.numTilings(100)
print A.numTilings(700)