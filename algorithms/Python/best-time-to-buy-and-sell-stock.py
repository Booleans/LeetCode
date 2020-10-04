'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

# Time: O(n), only 1 pass is used
# Space: O(1), only 2 variables used

def maxProfit(prices):
    '''
    :type prices: List[int]
    :rtype: int
    '''
    # If we are given no prices or just 1 price then profit is $0.
    if len(prices) <= 1:
        return 0

    buy = prices[0]
    profit = 0
    
    for price in prices[1:]:
        profit = max(profit, price - buy)
        # If this price is less than our previous purchase price, let's make it the new purchase price.
        buy = min(buy, price)
    return profit
        