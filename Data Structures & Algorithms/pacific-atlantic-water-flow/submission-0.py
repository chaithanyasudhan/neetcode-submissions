class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        r=len(heights)
        c=len(heights[0])
        p=deque()#diff queue to manage both seas
        pset=set()#to manage visited
        a=deque()
        aset=set()
        res=[]
        for i in range(r):
            p.append((i,0))
            pset.add((i,0))
            a.append((i,c-1))
            aset.add((i,c-1))

        for j in range(c):
            p.append((0,j))
            pset.add((0,j))
            a.append((r-1,j))
            aset.add((r-1,j))
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        while p :
            i,j=p.popleft()
            for di,dj in d:
                ni=i+di
                nj=j+dj
                if ni<0 or ni>=r or nj<0 or nj>=c or (ni,nj)in pset:
                    continue
                if heights[ni][nj]>=heights[i][j]:#checking from sea to source 
                    p.append((ni,nj))
                    pset.add((ni,nj))
        while a :
            i,j=a.popleft()
            for di,dj in d:
                ni=i+di
                nj=j+dj
                if ni<0 or ni>=r or nj<0 or nj>=c or (ni,nj)in aset:
                    continue
                if heights[ni][nj]>=heights[i][j]:#checking from sea to source 
                    a.append((ni,nj))
                    aset.add((ni,nj))
        for i in range(r):
            for j in range(c):
                if (i,j)in pset and (i,j)in aset:
                    res.append((i,j))
        return res