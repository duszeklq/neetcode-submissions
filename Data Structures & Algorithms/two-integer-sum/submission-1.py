class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for j in range(len(nums) - 1):
            for i in range(j, len(nums) - 1):
                if nums[j] + nums[i + 1] == target: 
                     return [j, i + 1]
            
# Brute force method
# Time Complexity: O(n^2)
# Space Complexity: O(1)