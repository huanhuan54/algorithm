# 算法与数据结构自学记录

这个仓库记录我自学算法与数据结构的过程。内容从基础数据结构开始，逐步扩展到二分、前缀和、排序、树、图搜索和动态规划，每个专题都配有文章、代码实现、测试用例和复盘记录。

## 学习内容

自学主题：算法与数据结构基础

目前已经整理了 13 个学习专题，并持续补充学习日志、错题复盘、代码实现和测试用例。仓库保留了按专题推进的提交记录，可以看到从基础查找到树、图搜索、二分答案、贪心和并查集的迭代过程。

文章与代码位于：

[algorithm-self-study](algorithm-self-study/)

学习过程记录：

[algorithm-self-study/LEARNING_LOG.md](algorithm-self-study/LEARNING_LOG.md)

错题与复盘：

[algorithm-self-study/REVIEW_NOTES.md](algorithm-self-study/REVIEW_NOTES.md)

提交记录整理：

[algorithm-self-study/COMMIT_SUMMARY.md](algorithm-self-study/COMMIT_SUMMARY.md)

后续学习路线：

[algorithm-self-study/STUDY_ROADMAP.md](algorithm-self-study/STUDY_ROADMAP.md)

## 专题文章

- 算法学习路线与复杂度分析
- 数组、滑动窗口与双指针
- 栈与队列：从括号匹配到单调栈
- 哈希表：用空间换时间
- 递归、搜索与回溯
- 动态规划入门：状态、转移与边界
- 前缀和：把区间求和变成一次查询
- 排序基础：从简单排序到归并排序
- 树的遍历：递归和层序两种视角
- 图搜索：BFS 与 DFS
- 二分答案：在答案范围里查找
- 贪心算法：每一步做局部最优选择
- 并查集：维护动态连通关系

## 验证方式

```bash
cd algorithm-self-study
python -m unittest discover -s tests
```
