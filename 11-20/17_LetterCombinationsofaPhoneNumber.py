def letterCombinations(digits):
    if not digits:
        return []
    digitMap = {'2': "abc",
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': "tuv",
                '9': "wxyz"}
    alphabets = [digitMap[x] for x in digits]
    outputs = [x for x in alphabets[0]]
    for i in range(1, len(alphabets)):
        newOutput = []
        for j in outputs:
            for k in alphabets[i]:
                newOutput.append(j + k)
        outputs = newOutput
    return outputs


print(letterCombinations('799'))

"""暴力循环"""
"""对于所有暴力for循环，都可以由backtracking进行更加工整
   的重写。本代码不多赘述，回溯算法于下文注释"""
