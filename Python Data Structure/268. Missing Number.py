from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        sum2 = 0
        ans = 0
        for i in range(0, n+1):
            if i < n:
               sum1 += nums[i] 
            sum2 += i
            ans = sum2 - sum1
        return ans

