def climb_stairs(n):
    if n <= 0:
        return 0
    if n <= 2:
        return n

    previous, current = 1, 2
    for _ in range(3, n + 1):
        previous, current = current, previous + current
    return current


def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        best = max(best, price - min_price)
        min_price = min(min_price, price)
    return best


def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)
    for right in range(len(nums)):
        for left in range(right):
            if nums[left] < nums[right]:
                dp[right] = max(dp[right], dp[left] + 1)
    return max(dp)
