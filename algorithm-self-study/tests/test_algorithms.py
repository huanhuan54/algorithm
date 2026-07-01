import unittest

from src.arrays import max_sum_subarray, two_sum_sorted
from src.backtracking import permutations, subsets
from src.dynamic_programming import climb_stairs, length_of_lis, max_profit
from src.hash_table import first_unique_char, two_sum
from src.prefix_sum import build_prefix_sum, range_sum, subarray_sum_count
from src.search import binary_search, linear_search, lower_bound, search_insert_position, upper_bound
from src.sorting import insertion_sort, merge_sort, selection_sort
from src.stack_queue import is_valid_parentheses, next_greater_elements
from src.tree import TreeNode, inorder, level_order, postorder, preorder


class AlgorithmTests(unittest.TestCase):
    def test_search(self):
        nums = [1, 3, 5, 7, 9]
        self.assertEqual(linear_search(nums, 7), 3)
        self.assertEqual(binary_search(nums, 7), 3)
        self.assertEqual(binary_search(nums, 2), -1)
        repeated = [1, 2, 2, 2, 5]
        self.assertEqual(lower_bound(repeated, 2), 1)
        self.assertEqual(upper_bound(repeated, 2), 4)
        self.assertEqual(search_insert_position([1, 3, 5, 6], 2), 1)

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

    def test_prefix_sum(self):
        self.assertEqual(build_prefix_sum([2, -1, 3]), [0, 2, 1, 4])
        self.assertEqual(range_sum([2, -1, 3, 4], 1, 3), 6)
        self.assertEqual(subarray_sum_count([1, 1, 1], 2), 2)
        self.assertEqual(subarray_sum_count([1, -1, 0], 0), 3)

    def test_sorting(self):
        nums = [5, 2, 4, 6, 1, 3]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(selection_sort(nums), expected)
        self.assertEqual(insertion_sort(nums), expected)
        self.assertEqual(merge_sort(nums), expected)
        self.assertEqual(nums, [5, 2, 4, 6, 1, 3])

    def test_tree_traversal(self):
        root = TreeNode(
            1,
            left=TreeNode(2, TreeNode(4), TreeNode(5)),
            right=TreeNode(3),
        )
        self.assertEqual(preorder(root), [1, 2, 4, 5, 3])
        self.assertEqual(inorder(root), [4, 2, 5, 1, 3])
        self.assertEqual(postorder(root), [4, 5, 2, 3, 1])
        self.assertEqual(level_order(root), [[1], [2, 3], [4, 5]])


if __name__ == "__main__":
    unittest.main()
