# Better Complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0, n):
            remain = target - nums[i]
            if remain in hash_map:
                return [hash_map[remain], i]
            hash_map[nums[i]] = i
            


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(0, n - 1):
#             for j in range(i + 1, n):
#                 if target == nums[i] + nums[j]:
#                     return[i, j]
                



