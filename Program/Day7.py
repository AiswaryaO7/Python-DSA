class Solution(object):
    def findJudge(self, n, trust):
        count = [0] * (n + 1)
        for a, b in trust:
            count[a] -= 1
            count[b] += 1
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i

        return -1
obj = Solution()
n = 3
trust = [[1,3],[2,3]]
print(obj.findJudge(n, trust))

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch, "", 1)

        return True
obj = Solution()
ransomNote = "aa"
magazine = "aab"
print(obj.canConstruct(ransomNote, magazine))

class Solution(object):
    def numIslands(self, grid):
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
obj = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(obj.numIslands(grid))
