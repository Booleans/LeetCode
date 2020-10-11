'''
Given an array of integers that is already sorted in ascending order, find two 
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2.
'''

def twoSum(numbers, target):
    # Use a left and right pointer to keep track of which index we're looking at.
    i_left = 0
    i_right = len(numbers) - 1
    
    while True:
        # Grab the numbers at our current left and right index.
        left = numbers[i_left]
        right = numbers[i_right]
        difference = target - (left + right)
        # If the difference is greater than 0 then we need the sum of the left and right number to be higher.
        # Since the array is sorted this means moving the left pointer to the right by 1 index position.
        if difference > 0:
            i_left += 1
        # To decrease our sum we'd want to move the right pointer to the left.
        elif difference < 0:
            i_right -= 1
        else: 
            # For some reason we're supposed to use 1 based indexing so add 1 to the index numbers.
            return [i_left + 1, i_right + 1]
            