import math


def can_ship_with_capacity(weights, days, capacity):
    used_days = 1
    current = 0

    for weight in weights:
        if weight > capacity:
            return False
        if current + weight > capacity:
            used_days += 1
            current = 0
        current += weight

    return used_days <= days


def ship_within_days(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        if can_ship_with_capacity(weights, days, mid):
            right = mid
        else:
            left = mid + 1

    return left


def min_eating_speed(piles, hours):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        needed = sum(math.ceil(pile / mid) for pile in piles)
        if needed <= hours:
            right = mid
        else:
            left = mid + 1

    return left
