class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        target_moves_away = abs(target[0]) + abs(target[1])

        for g in ghosts:
            if abs(g[0]-target[0]) + abs(g[1]-target[1]) <= target_moves_away:
                return False

        return True

A = Solution()


ghosts = [[1, 0], [0, 3]]
target = [0, 1]
print A.escapeGhosts(ghosts, target)

ghosts = [[1, 0]]
target = [2, 0]
print A.escapeGhosts(ghosts, target)

ghosts = [[2, 0]]
target = [1, 0]
print A.escapeGhosts(ghosts, target)

ghosts = [[1,9],[2,-5],[3,8],[9,8],[-1,3]]
target = [8,-10]
print A.escapeGhosts(ghosts, target)