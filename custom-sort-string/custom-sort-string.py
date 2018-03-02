class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        S = list(S)
        T = list(T)
        p = 0

        # Don't need to check the last one
        for i in range(len(S) - 1):
            s = S[i]

            for j in range(p, len(T)):
                t = T[j]

                if t == s:
                    # Swap
                    T[p], T[j] = T[j], T[p]
                    p += 1

        return "".join(T)