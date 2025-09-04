from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
     
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
            
        suffix = 1
        for j in range(n - 2, -1, -1):
            suffix *= nums[j + 1]
            ans[j] *= suffix


        return ans
    
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))




# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix = [1] * n
#         suffix = [1] * n
#         ans = [1] * n
     

#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]

#         for j in range(n - 2, -1, -1):
#             suffix[j] = suffix[j + 1] * nums[j + 1]

#         for k in range(n):
#             ans[k] = prefix[k] * suffix[k]


#         return ans
    
# sol = Solution()
# print(sol.productExceptSelf([1, 2, 3, 4]))


# COMPLEXITY O(n^^2)
# class Solution:
#     def multiplyAll(self, nums: List[int]) -> List[int]:
#         ans = []
#         n = len(nums)
#         for i in range(n):
#             mul = 1
#             for j in range(n):
#                 if nums[i] != nums[j]:
#                     mul *= nums[j]
#             ans.append(mul)
#         return ans


# sol = Solution()
# print(sol.multiplyAll([1, 2, 3, 4]))









# This is not allowed in this problem
# from typing import List

# class Solution:
#     def multiplyAll(self, nums: List[int]) -> List[int]:
#         mul = 1
#         ans = []
#         for i in range(len(nums)):
#             mul *= nums[i]

#         for i in range(len(nums)):
#             ans.append(mul // nums[i])
        
#         return ans

# sol = Solution()
# print(sol.multiplyAll([1, 2, 3, 4]))