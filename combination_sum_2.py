# -*- coding:utf8 -*-
#  Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
#
#     All numbers (including target) will be positive integers.
#     Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#     The solution set must not contain duplicate combinations.
#
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.ret = set([])
        candidates.reverse()
        self.search(target, candidates, [])
        return list([list(t) for t in self.ret])

    def search(self, remainSum, candidates, combList):
        i = 0
        while i < len(candidates):
            num = candidates[i]
            if num < remainSum:
                new_candidates = candidates[:]
                new_candidates.remove(num)
                self.search(remainSum - num, new_candidates, [num] + combList)
            elif num == remainSum:
                self.ret.add(tuple(sorted([remainSum] + combList)))
                # del candidates[i]
            else:
                del candidates[i]
                continue
            i += 1

class Solution2:
    def combinationSum2(self, candidates, target):
        self.ret = set([])
        stack = [(target, candidates, [])]

        while stack:
            cur_tup = stack.pop()
            remainSum = cur_tup[0]
            candidates = cur_tup[1]
            combList = cur_tup[2]

            if remainSum in candidates:
                self.ret.add(tuple(sorted([remainSum] + combList)))

            candidates = filter(lambda x:x<remainSum, candidates)

            for num in candidates:
                new_remain_sum = remainSum - num
                new_candidates = candidates[:]
                new_candidates.remove(num)
                new_combList = [num] + combList
                stack.append((new_remain_sum, new_candidates, new_combList))

        return list([list(t) for t in self.ret])

class Solution3:
    def combinationSum2(self, candidates, target):
        ans = []
        candidates.sort()
        for i, e in enumerate(candidates):
            if e < target:
                sublist = self.combinationSum2(candidates[i+1:], target - e)
                if sublist:
                    ans += [[e] + lis for lis in sublist if [e] + lis not in ans]
            elif e == target:
                if [e] not in ans:
                    ans += [[e]]
            else:
                break
        return ans

class Solution4:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        table = [None] + [set() for i in range(target)]
        print table
        for i in candidates:
            if i > target:
                break
            for j in range(target - i, 0, -1):
                table[i + j] |= {elt + (i,) for elt in table[j]}
            table[i].add((i,))
        return map(list, table[target])


candidates = [10,1,2,7,6,1,5]

target = 6

print Solution4().combinationSum2(candidates, target)
