# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2021/7/8 11:58 上午
# @Author  : lidong@test.com
# @Site    : 
# @File    : myself.py
"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：
    输入：nums1 = [1,3], nums2 = [2]
    输出：2.00000
    解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
    输入：nums1 = [1,2], nums2 = [3,4]
    输出：2.50000
    解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
    输入：nums1 = [0,0], nums2 = [0,0]
    输出：0.00000

示例 4：
    输入：nums1 = [], nums2 = [1]
    输出：1.00000

示例 5：
    输入：nums1 = [2], nums2 = []
    输出：2.00000

提示：
    - nums1.length == m
    - nums2.length == n
    - 0 <= m <= 1000
    - 0 <= n <= 1000
    - 1 <= m + n <= 2000
    - -10^6 <= nums1[i], nums2[i] <= 10^6

"""
from typing import List


class Solution:
    """

    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


if __name__ == '__main__':
    solution = Solution()
    # solution2 = Solution2()
    # solution3 = Solution3()
    nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    result = solution.findMedianSortedArrays(nums)
    print(result)
    # result = solution2.findMedianSortedArrays(nums)
    # print(result)
    # result = solution3.findMedianSortedArrays(nums)
    # print(result)
    #
    print()
    nums = [3, 2]
    result = solution.findMedianSortedArrays(nums)
    print(result)
    # result = solution2.findMedianSortedArrays(nums)
    # print(result)
    # result = solution3.findMedianSortedArrays(nums)
    # print(result)

    print()
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = solution.findMedianSortedArrays(nums)
    print(result)

    print()
    nums = [3, 3, 4]
    result = solution.findMedianSortedArrays(nums)
    print(result)
