class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
obj = Solution()
nums = [3, 0, 1]
print(obj.missingNumber(nums))

class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key in count:
            if count[key] > len(nums) // 2:
                return key
obj = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(obj.majorityElement(nums))

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
obj = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]

print(obj.merge(intervals))