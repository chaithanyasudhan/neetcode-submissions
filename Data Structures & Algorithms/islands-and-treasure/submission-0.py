class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #-1 shld be the base case
        #if 2147483647 continue 
        #min the dist nd store that val
        '''return 0 when reaching treasure but using dfs prevents using 
            teh same cell for shorter path hennce dfs not
        v=set()
        r=len(grid)
        c=len(grid[0])
        def dfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]==-1 or (i,j) in v  :
                return float('inf')
            v.add((i,j))
            if grid[i][j]==0:
                return 0
            return 1+min(dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1))
        for a in range(r):
            for b in range(c):
                if grid[a][b]==2147483647 and (a,b) not in v:
                    grid[a][b]=dfs(a,b)
        return grid'''
        from collections import deque
        r=len(grid)
        c=len(grid[0])
        q=deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    q.append((i,j))
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            i,j=q.popleft()
            for di,dj in d:
                ni=i+di
                nj=j+dj
                if ni<0 or ni>=r or nj<0 or nj>=c:
                    continue
                if grid[ni][nj]==2147483647:
                    grid[ni][nj]=1+grid[i][j]
                    q.append((ni,nj))
        return 
