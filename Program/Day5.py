#Stacks & Queues
#Valid Parentheses(20)
class Solution(object):
    def isValid(self, s):
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack and stack[-1] == d[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
obj = Solution()
s = "()[]{}"
print(obj.isValid(s))

#implement queue using stacks(232)
class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x):
        self.s1.append(x)
    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    def empty(self):
        return not self.s1 and not self.s2
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())    
print(q.pop())     
print(q.empty())   

#Daily temperature(739)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
obj = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(obj.dailyTemperatures(temperatures))

