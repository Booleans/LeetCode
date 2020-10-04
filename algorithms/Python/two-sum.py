'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# Time: O(n), only 1 pass is used
# Space: O(n) due to the dictionary used

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # A dictionary will allow is to keep track of the index that a number appeared at.
    mapper = {}

    for i, num in enumerate(nums):
        # What number do we need, given the target and current number?
        # We need the difference between the target and the current number.
        needed = target -  num
        if needed in mapper:
            return [mapper[needed], i]
        else:
            mapper[num] = i
        