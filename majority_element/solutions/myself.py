# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2021/7/8 11:58 上午
# @Author  : lidong@test.com
# @Site    : 
# @File    : myself.py
"""
17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 -1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。

示例 1：
    输入：[1,2,5,9,5,9,5,5,5]
    输出：5

示例 2：
    输入：[3,2]
    输出：-1

示例 3：
    输入：[2,2,1,1,1,2,2]
    输出：2

"""
from typing import List


class Solution:
    """
    """

    def majorityElement(self, nums: List[int]) -> int:
        pass



if __name__ == '__main__':
    solution = Solution()
    # solution2 = Solution2()
    # solution3 = Solution3()
    nums = [1, 0, 1, 0, 1]
    goal = 2
    result = solution.majorityElement(nums, goal)
    print(result)
    # result = solution2.majorityElement(nums, goal)
    # print(result)
    # result = solution3.majorityElement(nums, goal)
    # print(result)
    #
    print()
    nums = [0, 0, 0, 0, 0]
    goal = 0
    result = solution.majorityElement(nums, goal)
    print(result)
    # result = solution2.majorityElement(nums, goal)
    # print(result)
    # result = solution3.majorityElement(nums, goal)
    # print(result)
