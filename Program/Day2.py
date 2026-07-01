#Arrays &Strings
#best Time to buy and sell stock
class Solution(object):
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
obj = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(obj.maxProfit(prices))
    
#Remove Duplicates from Sorted array 
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
obj = Solution()
nums = [1, 1, 2, 2, 3, 4, 4]
k = obj.removeDuplicates(nums)
print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])

#Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in d:
                d[key] = []
            d[key].append(word)
        return list(d.values())
obj = Solution()
strs = ["listen","silence"]
print(obj.groupAnagrams(strs))
    