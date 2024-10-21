def intToRoman(num):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    text = ""
    for i in range(len(num_list)):
        while num >= num_list[i]:
            text += rom_list[i]
            num -= num_list[i]

    return text

print(intToRoman(1997))
"""列表匹配"""
"""对于有限，小量的样本，如罗马数字运算，可以使用穷举将对应的数字和符号
   作为列表储存起来，并且将输入值进行匹配。这样可以有效减少时间复杂度和
   代码难度"""