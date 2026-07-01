import unittest

from src.arrays import max_sum_subarray, two_sum_sorted
from src.backtracking import permutations, subsets
from src.dynamic_programming import climb_stairs, length_of_lis, max_profit
from src.hash_table import first_unique_char, two_sum
from src.search import binary_search, linear_search
from src.stack_queue import is_valid_parentheses, next_greater_elements


class AlgorithmTests(unittest.TestCase):
    def test_search(self):
        nums = [1, 3, 5, 7, 9]
        self.assertEqual(linear_search(nums, 7), 3)
        self.assertEqual(binary_search(nums, 7), 3)
        self.assertEqual(binary_search(nums, 2), -1)

    def test_arrays(self):
        self.assertEqual(two_sum_sorted([1, 2, 4, 6, 10], 8), [1, 3])
        self.assertEqual(max_sum_subarray([2, 1, 5, 1, 3, 2], 3), 9)

    def test_stack_queue(self):
        self.assertTrue(is_valid_parentheses("([]){}"))
        self.assertFalse(is_valid_parentheses("([)]"))
        self.assertEqual(next_greater_elements([2, 1, 2, 4, 3]), [4, 2, 4, -1, -1])

    def test_hash_table(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(first_unique_char("leetcode"), 0)
        self.assertEqual(first_unique_char("aabb"), -1)

    def test_backtracking(self):
        self.assertEqual(len(subsets([1, 2, 3])), 8)
        self.assertEqual(sorted(permutations([1, 2])), [[1, 2], [2, 1]])

    def test_dynamic_programming(self):
        self.assertEqual(climb_stairs(5), 8)
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)


if __name__ == "__main__":
    unittest.main()
