def subsets(nums):
    result = []
    path = []

    def dfs(start):
        result.append(path[:])
        for index in range(start, len(nums)):
            path.append(nums[index])
            dfs(index + 1)
            path.pop()

    dfs(0)
    return result


def permutations(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            result.append(path[:])
            return

        for index, value in enumerate(nums):
            if used[index]:
                continue
            used[index] = True
            path.append(value)
            dfs()
            path.pop()
            used[index] = False

    dfs()
    return result
