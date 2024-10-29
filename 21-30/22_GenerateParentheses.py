from collections import Counter


def generateParenthesis(n):
    res = []

    def backtracking(comb):
        if len(comb) / 2 == n:
            res.append(comb)
            return
        counts = Counter(comb)
        if counts['('] > counts[')']:
            backtracking(comb + ')')
        if counts['('] < n:
            backtracking(comb + '(')

    backtracking('(')
    return res


"""回溯算法"""
"""回溯算法的小复习，日后多加联系回溯算法
   根据leetcode最快的算法，在backtracking中使用Unplaced和unclosed来代替count,这里就不再多写了"""
