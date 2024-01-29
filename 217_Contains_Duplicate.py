# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1: Compare each number to the others. Time: O(n²) Space:O(1)
        # Solution 2: Sorting. Time: O(n logn) Space:O(1)
        # Solution 3: Hashset.Time: O(n) Space:O(n) 【√】
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# 开一个新的hashset，将distinct的value放入hashset中。因为hashset不允许重复的元素，因此可以快速插入，删除，查询，时间是O(1)。hashset是无序的。

