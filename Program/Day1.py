 #two sum
class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i, num in enumerate(nums):
            comp=target-num
            if comp in seen:
                return[seen[comp],i]
            seen[num]=i
        return[]
obj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(obj.twoSum(nums, target))
    
#palindrome number
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original = x
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        return original == reverse
obj = Solution()
x = 121
print(obj.isPalindrome(x))

#longest substring without repeating characters 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len
obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))
