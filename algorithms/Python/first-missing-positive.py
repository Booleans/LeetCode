'''
https://leetcode.com/problems/first-missing-positive/ (Hard)

Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
'''

def firstMissingPositive(nums):
    # The number of possible positive integers in the list is the length of the list.
    # And let's include 0 so that a number matches its index in the list.
    possible_positives = range(len(nums)+1)
    seen = [False for _ in possible_positives]
    # We set 0 to True (seen) since we only added it to make the index positions match.
    seen[0] = True
    
    for num in nums:
        if num in possible_positives:
            seen[num] = True
    
    for i, seen in enumerate(seen):
        if not seen:
            return i
    else:
        return max(possible_positives) + 1
