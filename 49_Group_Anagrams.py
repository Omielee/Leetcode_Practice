# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1:Sort. Time :m*nLog(n),m is the length of how many strings in the array
        # Solution 2: Counting the character of each.Hashmap key:value = [1e:1a:1t]:[eat,tea,ate] Time:O(m*n)
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 #a-z
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()