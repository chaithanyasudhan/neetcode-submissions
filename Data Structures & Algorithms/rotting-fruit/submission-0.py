class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multisource bfs
        from collections import deque
        r=len(grid)
        c=len(grid[0])
        q=deque()
        c1=0
        f=0#count for fresh
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    f+=1
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and f>0:#f>0 so that it doesnt run an extra loop for count
            s=len(q)
            for _ in range(s):
                i,j=q.popleft()
                for ni,nj in d:
                    di=i+ni
                    dj=j+nj
                    if di<0 or di>=r or dj<0 or dj>=c or grid[di][dj]==0:
                        continue
                    if grid[di][dj]==1:
                        grid[di][dj]=2
                        f-=1
                        q.append((di,dj))
                
            c1+=1
        if f>0:
            return -1
        return c1