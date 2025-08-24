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


# Using C++
# class Solution {
# public:
#     int missingNumber(vector<int>& nums) {
#         int ans = 0;
#         int n = nums.size();
#         for (int i = 0; i < n; i++) {
#             ans ^= nums[i];
#         }
        
#         for (int i = 1; i <= n; i++) {
#             ans ^= i;
#         }
#         return ans; 
#     }
# };