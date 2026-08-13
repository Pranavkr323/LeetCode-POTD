# LeetCode POTD - 2026-08-13
# Problem 2213 - Longest Substring of One Repeating Character
# Approach: Segment Tree

class Solution:
            

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        class Node:
            def __init__(self, lc='', rc='', pre=0, suf=0, best=0, length=0):
                self.lc = lc
                self.rc = rc
                self.pre = pre
                self.suf = suf
                self.best = best
                self.length = length

        def merge(a, b):
                if a.length == 0:
                    return b
                if b.length == 0:
                    return a

                res = Node()

                res.lc = a.lc
                res.rc = b.rc
                res.length = a.length + b.length

                res.pre = a.pre
                res.suf = b.suf
                res.best = max(a.best, b.best)

                if a.rc == b.lc:
                    res.best = max(res.best, a.suf + b.pre)

                    if a.pre == a.length:
                        res.pre = a.length + b.pre

                    if b.suf == b.length:
                        res.suf = b.length + a.suf

                return res

        def build(node, l, r):
            if l == r:
                tree[node] = Node(
                    s[l], s[l], 1, 1, 1, 1
                )
                return

            mid = (l + r) // 2

            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)

            tree[node] = merge(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = Node(ch, ch, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(2 * node + 1, l, mid, idx, ch)
            else:
                update(2 * node + 2, mid + 1, r, idx, ch)

            tree[node] = merge(
                tree[2 * node + 1],
                tree[2 * node + 2]
            )

        s = list(s)
        tree = [None] * (4 * len(s))
        build(0, 0, len(s) - 1)
        n = len(queryCharacters)
        ans = []

        for i in range(n):
            c_to_change = queryCharacters[i]
            update(0,0, len(s)-1, queryIndices[i], c_to_change)   
            ans.append(tree[0].best)

        return ans
