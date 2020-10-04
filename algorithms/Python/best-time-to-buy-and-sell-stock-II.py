'''
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

# Time: O(n), only 1 pass is used
# Space: O(1), only 3 variables used

def maxProfit(prices):
    '''
    :type prices: List[int]
    :rtype: int
    '''
    # If we don't have at least 2 price then no profit is possible.
    if len(prices) < 2:
        return 0
    
    buy = prices[0]
    profit = 0
    # I am going to keep track of the previous price seen as I loop through the array.
    # If a number is lower than the previous price, that indicates we could sell for a profit.
    previous = buy

    for price in prices[1:]:
        if price < previous:
            profit += previous - buy
            buy = price
        previous = price
    # We also need to account for the end of the array.
    # Our previous loop will fail to sell at the end of the array so we need an additional check.
    if prices[-1] >= prices[-2] and prices[-1] > buy:
        profit += prices[-1] - buy
    return profit
        