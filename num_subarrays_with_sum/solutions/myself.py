# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2021/7/8 11:58 上午
# @Author  : lidong@test.com
# @Site    : 
# @File    : myself.py
"""
930. 和相同的二元子数组
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。子数组 是数组的一段连续部分

示例 1：
    输入：nums = [1,0,1,0,1], goal = 2
    输出：4
    解释：
    有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]

示例 2：
    输入：nums = [0,0,0,0,0], goal = 0
    输出：15

提示：
    - 1 <= nums.length <= 3 * 104
    - nums[i] 不是 0 就是 1
    - 0 <= goal <= nums.length
"""
from typing import List


class Solution:
    """
    耗时过长
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        for index in range(len(nums)):
            _sum = 0 + nums[index]
            if _sum == goal:
                count += 1
            for after in range(index + 1, len(nums)):
                _sum += nums[after]
                if _sum == goal:
                    count += 1
        return count


class Solution2:
    """
    参考题解，遇0则记，遇1则开始加直到等于 goal 后开始记后续的 0，遇1则算，且开始记count
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        left_zero = 0
        right_zero = 0
        _sum = 0
        for num in nums:
            if num == 0 and _sum == 0:
                left_zero += 1
            elif num == 0 and _sum == goal:
                right_zero += 1
            elif num == 1 and _sum == goal:
                print({
                    "left_zero": left_zero,
                    "right_zero": right_zero
                })
                count += (left_zero + 1) * (right_zero + 1)
                left_zero = 0
                right_zero = 0
                _sum = 0
            else:
                _sum += 1
        return count


class Solution3:
    """
    参考题解，记下所有1前面的0的个数放入一个数组里，然后再新的数组里 每隔 goal 取出来相乘
    """

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        zero_count_list = []
        _sum = 0
        for num in nums:
            if num == 0:
                _sum += 1
            else:
                zero_count_list.append(_sum + 1)
                _sum = 0
        zero_count_list.append(_sum + 1)

        if goal == 0:
            for c in zero_count_list:
                count += (c * (c - 1)) // 2
            return count

        index = 0
        while index + goal < len(zero_count_list):
            count += zero_count_list[index] * zero_count_list[index + goal]
            index += 1

        return count


if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    result = solution.numSubarraysWithSum(nums, goal)
    print(result)
    result = solution2.numSubarraysWithSum(nums, goal)
    print(result)
    result = solution3.numSubarraysWithSum(nums, goal)
    print(result)

    print()
    nums = [0, 0, 0, 0, 0]
    goal = 0
    result = solution.numSubarraysWithSum(nums, goal)
    print(result)
    result = solution2.numSubarraysWithSum(nums, goal)
    print(result)
    result = solution3.numSubarraysWithSum(nums, goal)
    print(result)
