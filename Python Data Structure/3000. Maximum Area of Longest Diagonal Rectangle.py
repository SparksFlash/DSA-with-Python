import math
from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        area = 0
        for length, width in dimensions:
            cur_diagonal = math.sqrt(length ** 2 + width ** 2)
            if cur_diagonal > max_diagonal:
                area = length * width
                max_diagonal = cur_diagonal
            elif max_diagonal == cur_diagonal:
                area = max(area, length * width)
                
        return area