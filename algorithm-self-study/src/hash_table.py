from collections import Counter


def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], index]
        seen[value] = index
    return []


def first_unique_char(text):
    counts = Counter(text)
    for index, char in enumerate(text):
        if counts[char] == 1:
            return index
    return -1
