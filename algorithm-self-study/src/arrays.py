def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


def max_sum_subarray(nums, window_size):
    if window_size <= 0 or window_size > len(nums):
        raise ValueError("window_size must be between 1 and len(nums)")

    current = sum(nums[:window_size])
    best = current
    for right in range(window_size, len(nums)):
        current += nums[right] - nums[right - window_size]
        best = max(best, current)
    return best
