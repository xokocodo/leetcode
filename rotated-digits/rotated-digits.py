class Solution(object):

    def __init__(self):
        self.answers = [0 for x in range(10000)]
        self.m = 1

        self.bad = [3, 4, 7]
        self.good = [2, 5, 6, 9]

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        for i in range(self.m, N + 1):

            g = False
            n = i

            while True:

                if (n % 10) in self.good:
                    g = True

                if (n % 10) in self.bad:
                    g = False
                    break

                if n == 0:
                    break

                n = n / 10

            if g:
                self.answers[i] = self.answers[i - 1] + 1
            else:
                self.answers[i] = self.answers[i - 1]

        return self.answers[N]