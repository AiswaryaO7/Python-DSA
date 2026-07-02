class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
obj = Solution()
nums = [1, 2, 3, 1]
print(obj.containsDuplicate(nums))

class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
obj = Solution()
s = "anagram"
t = "nagaram"
print(obj.isAnagram(s, t))

