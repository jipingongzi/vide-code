#!/usr/bin/env python3
"""
数字排序项目主程序
演示如何使用数字排序模块
"""

from src.number_sorter import sort_numbers


def main():
    """主函数"""
    print("=== 数字排序演示 ===")

    # 示例数字列表
    numbers = [42, 15, 73, 28, 91, 56, 37, 84, 19, 62]

    print(f"原始数字: {numbers}")

    # 演示不同排序算法
    algorithms = ['builtin', 'quick', 'merge', 'bubble']

    for algo in algorithms:
        try:
            sorted_numbers = sort_numbers(numbers, algorithm=algo)
            print(f"\n{algo} 算法排序结果: {sorted_numbers}")
        except ValueError as e:
            print(f"\n{algo} 算法错误: {e}")

    # 用户交互示例
    print("\n=== 自定义排序 ===")

    try:
        # 获取用户输入的数字
        user_input = input("请输入要排序的数字（用空格分隔）: ")
        if user_input.strip():
            user_numbers = [float(num) if '.' in num else int(num) for num in user_input.split()]
            print(f"您的数字: {user_numbers}")

            # 选择算法
            algo_input = input("选择排序算法 (builtin/quick/merge/bubble，默认为 builtin): ").strip().lower()
            if not algo_input:
                algo_input = 'builtin'

            sorted_user_numbers = sort_numbers(user_numbers, algorithm=algo_input)
            print(f"排序结果: {sorted_user_numbers}")
        else:
            print("未输入数字，跳过自定义排序。")

    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()