# 自学算法系列

本仓库用于记录个人自学算法与数据结构的过程，内容包含学习路线、技术文章、配套代码和测试用例。系列文章围绕常见算法能力展开：复杂度分析、数组与双指针、栈与队列、哈希表、递归与回溯、动态规划。

## 学习目标

- 掌握常见数据结构的使用场景和复杂度特征。
- 能够把题目转化为可实现的算法步骤。
- 通过代码和测试验证算法正确性。
- 形成持续复盘的学习记录，便于后续补充 commit 记录和更多专题。

## 文章目录

1. [算法学习路线与复杂度分析](articles/01_complexity_and_plan.md)
2. [数组、滑动窗口与双指针](articles/02_array_two_pointers.md)
3. [栈与队列：从括号匹配到单调栈](articles/03_stack_queue.md)
4. [哈希表：用空间换时间](articles/04_hash_table.md)
5. [递归、搜索与回溯](articles/05_recursion_backtracking.md)
6. [动态规划入门：状态、转移与边界](articles/06_dynamic_programming.md)
7. [前缀和：把区间求和变成一次查询](articles/07_prefix_sum.md)
8. [排序基础：从简单排序到归并排序](articles/08_sorting_basics.md)

## 代码结构

```text
articles/  技术文章
src/       算法实现
tests/     简单测试
```

## 运行测试

```bash
python -m unittest discover -s tests
```

## 后续计划

- 增加排序、二分查找、图论、并查集、最短路等专题。
- 将每次学习补充为独立 commit，形成持续学习轨迹。
- 为每个专题补充更多边界用例和错题复盘。
