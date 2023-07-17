nums = [2,7,9,3,1]

first, second = 0, 0

for house in nums:
    maximum = max(house + first, second) # (2+0, 0) | (7+0, 2) | (9+2, 7) | (3+7, 11) | (1+11, 11)
    first = second # 0 | 2 | 7 | 11 | 11
    second = maximum # 2 | 7 | 11 | 11 | 12

print(second)


from typing import List

class Solution:
    def choise(self, nums: List[int]) -> int:
        return max(self.rob(nums[1:]), self.rob(nums[:-1]))


    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for num in nums:
            temp = max(num+first, second)
            first, second = second, temp
            
        return second
    
# nums = [1,2,3]
# nums = [1,2,3,1]

nums = [2,3,2]
test = Solution()
print(test.choise(nums))