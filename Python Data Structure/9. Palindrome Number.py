from typing import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while temp > 0:
            rem = temp % 10
            reverse = (reverse * 10) + rem
            temp = temp // 10
        if x == reverse:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome(121))



        
