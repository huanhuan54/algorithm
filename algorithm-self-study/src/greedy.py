def max_non_overlapping_intervals(intervals):
    if not intervals:
        return 0

    ordered = sorted(intervals, key=lambda item: item[1])
    count = 0
    last_end = None

    for start, end in ordered:
        if last_end is None or start >= last_end:
            count += 1
            last_end = end

    return count


def can_jump(nums):
    farthest = 0
    for index, step in enumerate(nums):
        if index > farthest:
            return False
        farthest = max(farthest, index + step)
    return True


def max_profit_many_transactions(prices):
    profit = 0
    for index in range(1, len(prices)):
        if prices[index] > prices[index - 1]:
            profit += prices[index] - prices[index - 1]
    return profit
