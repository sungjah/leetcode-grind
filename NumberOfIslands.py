class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0

        def bfs(row, col):
            q = collections.deque()
            visit.add((row,col))
            q.append((row,col))

            while q:
                curr_row, curr_col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    if ((curr_row + dr) in range(rows) and (curr_col + dc) in range(cols) and
                    grid[curr_row+dr][curr_col+dc] == "1" and (curr_row+dr, curr_col+dc) not in visit):
                        q.append((curr_row+dr, curr_col+dc))
                        visit.add((curr_row+dr, curr_col+dc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    bfs(row,col)
                    islands += 1
        return islands