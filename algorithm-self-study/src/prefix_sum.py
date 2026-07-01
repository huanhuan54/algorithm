from collections import defaultdict


def build_prefix_sum(nums):
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)
    return prefix


def range_sum(nums, left, right):
    if left < 0 or right >= len(nums) or left > right:
        raise ValueError("invalid range")

    prefix = build_prefix_sum(nums)
    return prefix[right + 1] - prefix[left]


def subarray_sum_count(nums, target):
    counts = defaultdict(int)
    counts[0] = 1
    current = 0
    total = 0

    for value in nums:
        current += value
        total += counts[current - target]
        counts[current] += 1

    return total
