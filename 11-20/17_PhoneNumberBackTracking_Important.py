def Phone(digits):
    if not digits:
        return []
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(idx, comb):
        if idx == len(digits):
            res.append(comb[:])
            return

        for letter in digit_to_letters[digits[idx]]:
            backtrack(idx + 1, comb + letter)

    res = []
    backtrack(0, "")

"""回溯算法（BackTracking)"""
"""回溯算法的本质就是多层嵌套for循环，通过遍历每个节点的子节点并且将数据收集至res来完成目标。
   在这个回溯算法中，层数=digit的数量，这个是由idx == len(digit)达成的，idx在本算法中有
   两个用处，一，控制最后字符串的大小(由len完成)，二，控制层数的不同的数字(由digits[idx]完
   成。在主要的for循环中，backtrack(idx + 1, comb + letter)的意思便是在该层中，把对应
   的字符串的每个字母都添加到收到的comb中，将新的comb和进位的idx传给下游的子节点。该算法的
   逻辑并不难理解，但是对于新手来讲比较绕脑，需要多复习来加强记忆。"""
"""PS:回溯算法的基本结构由几部分构成，一，终止段，对值进行判断是否终止该节点并且返回该值，二，
   如果不终止，则对该值进行新一轮for循环"""