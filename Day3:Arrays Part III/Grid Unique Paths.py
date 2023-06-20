class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=[ [0] * m for _ in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if i==0 or j==0:
                    res[i][j]=1
                else:
                    res[i][j]= res[i-1][j]+res[i][j-1]
        return res[n-1][m-1]