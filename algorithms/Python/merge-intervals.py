'''
Given a collection of intervals, merge all overlapping intervals.
'''

# Time: O(n log n), due to the sort
# Space: O(n)

def merge(intervals):
    '''
    :type intervals: List[int]
    :rtype: List[List[int]]
    '''
    if len(intervals) < 2:
        return intervals
    
    merged = []
    # Sort by the beginning of the interval.
    intervals.sort(key=lambda x: x[0])
    # Add the first interval into the merged array as a starting point. 
    merged.append(intervals[0])

    for interval in intervals[1:]:
        start = interval[0]
        end = interval[1]
        # If the starting time is before or the same as the end of the previous interval's end we can merge.
        if start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append(interval)

    return merged
