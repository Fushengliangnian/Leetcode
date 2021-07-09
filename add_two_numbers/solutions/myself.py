# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2021/7/8 11:58 上午
# @Author  : lidong@test.com
# @Site    : 
# @File    : myself.py
"""
2. 两数相加
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

提示：
    - 每个链表中的节点数在范围 [1, 100] 内
    - 0 <= Node.val <= 9
    - 题目数据保证列表表示的数字不含前导零


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
from add_two_numbers.common import ListNode


class Solution:

    @classmethod
    def calculate(cls, result_value, before_node, init_next_node=False):
        if result_value >= 10:
            before_node.val = result_value % 10
            before_node.next = ListNode(result_value // 10)
        else:
            before_node.val = result_value
            if init_next_node:
                before_node.next = ListNode()

    @classmethod
    def addTwoNumbers(cls, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode()
        before_node = None
        while True:
            if before_node is None:
                before_node = result_node

            result_value = l1.val + l2.val + before_node.val
            print(result_value)
            if l1.next is None and l2.next is None:
                cls.calculate(result_value, before_node)
                return result_node

            l1 = ListNode() if l1.next is None else l1.next
            l2 = ListNode() if l2.next is None else l2.next

            cls.calculate(result_value, before_node, True)

            before_node = before_node.next



if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    # print({
    #     "l1": l1.val,
    #     "l1_next": l1.next,
    #     "l1.next": l1.next.val,
    #     "l1.next.next": l1.next.next.val
    # })
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    node = Solution.addTwoNumbers(l1, l2)
    # print(node)
    while True:
        print(node.val)
        node = node.next
        if node is None:
            break

    l1 = ListNode()
    l2 = ListNode()

    node = Solution.addTwoNumbers(l1, l2)
    print()
    # print(node)
    while True:
        print(node.val)
        node = node.next
        if node is None:
            break

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, )))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, )))))

    node = Solution.addTwoNumbers(l1, l2)
    print()
    # print(node)
    while True:
        print(node.val)
        node = node.next
        if node is None:
            break
