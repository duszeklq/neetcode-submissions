class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
    
            if complement not in seen:
                seen[num] = i 
            else:
                return [seen[complement], i]
            
# Optimal solution
# Time Complexity: O(n)
# Space Complexity: O(n)