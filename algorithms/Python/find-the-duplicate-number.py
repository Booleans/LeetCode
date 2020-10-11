'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.
'''

def findDuplicate(nums):
    # The number of integers missing is the difference between the length of the original list
    # and the length of the set of the original list.
    unique_nums = set(nums)
    count_missing = len(nums) - len(unique_nums)
    sum_missing_numbers = sum(nums) - sum(unique_nums)
    # Since we know that there is only 1 distinct integer missing, we can find this integer by dividing the 
    # sum of the missing numbers by the number of missing numbers.
    return int(sum_missing_numbers/count_missing)
    