class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        # Memoization cache
        dp = {}
        
        def dfs(r, c, prev_val):
            # Base cases: out of bounds or not strictly increasing
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev_val:
                return 0
            
            # Return cached result if computed already
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            curr_val = matrix[r][c]
            
            # Explore all 4 directions
            res = max(res, 1 + dfs(r + 1, c, curr_val))
            res = max(res, 1 + dfs(r - 1, c, curr_val))
            res = max(res, 1 + dfs(r, c + 1, curr_val))
            res = max(res, 1 + dfs(r, c - 1, curr_val))
            
            # Store and return
            dp[(r, c)] = res
            return res

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c, -1))
                
        return longest