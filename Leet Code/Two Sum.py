from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Dictionary to store indices of elements
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            # Check if complement exists in the dictionary
            if complement in num_indices:
                # If found, return the indices
                return [num_indices[complement], i]
            # Otherwise, add the current element to the dictionary with its index
            num_indices[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1]