class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
obj = Solution()
n = 6
print(obj.fib(n))

class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
obj = Solution()
n = 5
print(obj.climbStairs(n))

class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return result
obj = Solution()
n = 3
print(obj.generateParenthesis(n))

