class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        P(m,n) = P(m-1,n) + P(m, n-1)
        P(0,n) = 1
        P(m,0) = 1
        """   
        P = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                P[col] += P[col - 1]
        return P[-1]
