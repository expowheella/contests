# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:

from operator import le
import re
from typing import List



# << ---- # Solution 1 ---- >>
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=list()
        result = 0
        for i in nums:
            result += i
            lst.append(result)
        return lst

test1 = Solution()
print(test1.runningSum([1,2,3,4]))
"""

#  << ---- # Solution 2 ---- >> """
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]


test1 = Solution()
print(test1.runningSum([1,2,3,4]))
