from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R = len(heights)
        C = len(heights[0])
        costmap = [[int(10e7)] * C for _ in range(R)]

        # 위 오 아래 왼
        dy = [-1,0,1,0]
        dx = [0,1,0,-1]

        hq = []
        heapq.heappush(hq, (0, 0, 0))
        while hq:
            now_max_height, r, c = heapq.heappop(hq)
            if (r, c) == (R-1, C-1):
                return now_max_height
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if not (0<=nr<R and 0<=nc<C): continue
                height_diff = abs(heights[r][c] - heights[nr][nc])
                max_height = max(now_max_height, height_diff)
                if max_height >= costmap[nr][nc]: continue
                heapq.heappush(hq,(max_height, nr, nc))
                costmap[nr][nc] = max_height




print(Solution.minimumEffortPath(None,[[1,2,2],[3,8,2],[5,3,5]]),2)
print(Solution.minimumEffortPath(None,[[1,2,3],[3,8,4],[5,3,5]]),1)
print(Solution.minimumEffortPath(None,[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]),0)