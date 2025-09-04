from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        current_cnt = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                current_cnt = 0
            else:
                current_cnt += 1
            
            if(ans < current_cnt):
                ans = current_cnt

        return ans



# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         max_ones = 0
#         ones = 0

#         for num in nums:
#             if num == 1:
#                 ones += 1
#             else:
#                 max_ones = max(ones, max_ones)
#                 ones = 0

#         max_ones = max(ones, max_ones)
#         return max_ones
