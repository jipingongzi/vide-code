"""
数字排序模块的单元测试
"""

import unittest
from number_sorter import (
    sort_numbers_builtin,
    quick_sort,
    merge_sort,
    bubble_sort,
    sort_numbers
)


class TestNumberSorter(unittest.TestCase):
    """测试数字排序功能"""

    def setUp(self):
        """测试前置设置"""
        self.test_cases = [
            ([], []),  # 空列表
            ([1], [1]),  # 单元素
            ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),  # 普通列表
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),  # 逆序
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # 已排序
            ([3.14, 2.71, 1.41, 2.0], [1.41, 2.0, 2.71, 3.14]),  # 浮点数
            ([-5, -1, -3, 0, 2, -2], [-5, -3, -2, -1, 0, 2]),  # 包含负数
        ]

    def test_sort_numbers_builtin(self):
        """测试内置排序"""
        for input_nums, expected in self.test_cases:
            with self.subTest(input=input_nums):
                result = sort_numbers_builtin(input_nums)
                self.assertEqual(result, expected)

    def test_quick_sort(self):
        """测试快速排序"""
        for input_nums, expected in self.test_cases:
            with self.subTest(input=input_nums):
                result = quick_sort(input_nums)
                self.assertEqual(result, expected)

    def test_merge_sort(self):
        """测试归并排序"""
        for input_nums, expected in self.test_cases:
            with self.subTest(input=input_nums):
                result = merge_sort(input_nums)
                self.assertEqual(result, expected)

    def test_bubble_sort(self):
        """测试冒泡排序"""
        for input_nums, expected in self.test_cases:
            with self.subTest(input=input_nums):
                result = bubble_sort(input_nums)
                self.assertEqual(result, expected)

    def test_sort_numbers_function(self):
        """测试主排序函数"""
        # 测试默认算法（builtin）
        numbers = [5, 1, 4, 2, 8]
        expected = [1, 2, 4, 5, 8]
        result = sort_numbers(numbers)
        self.assertEqual(result, expected)

        # 测试所有算法
        test_nums = [5, 1, 4, 2, 8]
        expected = [1, 2, 4, 5, 8]

        for algo in ['builtin', 'quick', 'merge', 'bubble']:
            with self.subTest(algorithm=algo):
                result = sort_numbers(test_nums, algorithm=algo)
                self.assertEqual(result, expected)

    def test_sort_numbers_invalid_algorithm(self):
        """测试无效算法名称"""
        with self.assertRaises(ValueError):
            sort_numbers([1, 2, 3], algorithm='invalid_algo')

    def test_sort_preserves_original_list(self):
        """测试原始列表不被修改"""
        original = [5, 1, 4, 2, 8]
        original_copy = original[:]

        # 所有排序函数都应返回新列表，不修改原列表
        sort_numbers_builtin(original)
        self.assertEqual(original, original_copy)

        quick_sort(original)
        self.assertEqual(original, original_copy)

        merge_sort(original)
        self.assertEqual(original, original_copy)

        bubble_sort(original)
        self.assertEqual(original, original_copy)

        sort_numbers(original, algorithm='builtin')
        self.assertEqual(original, original_copy)

    def test_sort_with_duplicates(self):
        """测试包含重复元素的排序"""
        numbers = [5, 2, 8, 2, 5, 1, 8]
        expected = [1, 2, 2, 5, 5, 8, 8]

        for algo in ['builtin', 'quick', 'merge', 'bubble']:
            with self.subTest(algorithm=algo):
                result = sort_numbers(numbers, algorithm=algo)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()