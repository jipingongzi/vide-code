"""
数字排序模块
提供多种数字排序算法的实现
"""

def sort_numbers_builtin(numbers):
    """
    使用Python内置排序函数进行排序

    Args:
        numbers: 数字列表（整数或浮点数）

    Returns:
        排序后的新列表
    """
    return sorted(numbers)


def quick_sort(numbers):
    """
    快速排序算法实现

    Args:
        numbers: 数字列表（整数或浮点数）

    Returns:
        排序后的新列表
    """
    if len(numbers) <= 1:
        return numbers[:]

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(numbers):
    """
    归并排序算法实现

    Args:
        numbers: 数字列表（整数或浮点数）

    Returns:
        排序后的新列表
    """
    if len(numbers) <= 1:
        return numbers[:]

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return _merge(left_sorted, right_sorted)


def _merge(left, right):
    """归并排序的合并步骤"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def bubble_sort(numbers):
    """
    冒泡排序算法实现

    Args:
        numbers: 数字列表（整数或浮点数）

    Returns:
        排序后的新列表
    """
    nums = numbers[:]
    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break

    return nums


def sort_numbers(numbers, algorithm='builtin'):
    """
    使用指定算法对数字进行排序

    Args:
        numbers: 数字列表（整数或浮点数）
        algorithm: 排序算法，可选值:
                  'builtin' (默认) - Python内置排序
                  'quick' - 快速排序
                  'merge' - 归并排序
                  'bubble' - 冒泡排序

    Returns:
        排序后的新列表

    Raises:
        ValueError: 当传入不支持的算法名称时
    """
    algorithms = {
        'builtin': sort_numbers_builtin,
        'quick': quick_sort,
        'merge': merge_sort,
        'bubble': bubble_sort
    }

    if algorithm not in algorithms:
        raise ValueError(f"不支持的算法: {algorithm}。支持: {list(algorithms.keys())}")

    return algorithms[algorithm](numbers)


if __name__ == "__main__":
    # 示例用法
    sample_numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始列表:", sample_numbers)

    for algo in ['builtin', 'quick', 'merge', 'bubble']:
        sorted_nums = sort_numbers(sample_numbers, algorithm=algo)
        print(f"{algo} 排序结果:", sorted_nums)