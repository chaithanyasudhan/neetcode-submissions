class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        v=set()
        s=0
        def dfs(a,b):
            if (a<0 or a>=r or b<0 or b>=c or (a,b) in v or grid[a][b]==0):
                return 0
            v.add((a,b))
            return (1+
            dfs(a+1,b)+
            dfs(a-1,b)+
            dfs(a,b+1)+
            dfs(a,b-1))
        for i in range(r):
            for j in range(c):
                if (i,j) not in v and grid[i][j]==1:
                    s=max(s,dfs(i,j))
        return s
