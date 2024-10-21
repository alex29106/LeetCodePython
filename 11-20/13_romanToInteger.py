def romanToInt(s):
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    num = 0
    while s != "":
        if s[:2] in rom_list:
            num += num_list[rom_list.index(s[:2])]
            s = s[2:]
        else:
            num += num_list[rom_list.index(s[0])]
            s = s[1:]
    return num


def romanToInt2(s):
    roman_to_int = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }
    num = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman_to_int:
            num += roman_to_int[s[i:i + 2]]
            i += 2
        else:
            num += roman_to_int[s[i]]
            i += 1
    return num


"""字典匹配"""
"""同上题，对小样本量问题同样可以使用字典作为匹配，在第一个算法中，使用.index()可能会
   造成一定的时间复杂度，所以使用词典并且用i作为已计算的s的长度来避免此类问题发生"""
