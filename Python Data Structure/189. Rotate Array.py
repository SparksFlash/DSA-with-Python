from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


    def reverse(self, nums, start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

sol = Solution()
print(sol.rotate([1, 2, 3, 4]))