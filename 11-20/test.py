# from collections import Counter
# nums = [1,1,1,2,2,2,3,3,4,5,6,6,6]
# count = Counter(nums)
#
# print(count)
# print(sorted(count))
# print(count[1])
# nums = [i for i in sorted(count) if i != 0]
# print(nums)
#
# for i,n in enumerate(nums):
#     print(i,n)


# digits = '2342'
# digitMap = {'2': "abc",
#             '3': "def",
#             '4': "ghi",
#             '5': "jkl",
#             '6': "mno",
#             '7': "pqrs",
#             '8': "tuv",
#             '9': "wxyz"}
#
# alphabets = [digitMap[x] for x in digits]



# a = 'abc'
# b = 'def'
# result = []
# for i in a:
#     for j in b:
#         result.append(i+j)
#
# print(result)


# from collections import Counter
#
# nums = [1,1,1,2,3,3,4,6]
# counts = Counter(nums)
# print(counts)
# print(counts[1.23123])

# nums = [1]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         print(j)

validDict = ["[]", "()", "{}"]
s = "{wd}[()]"
print(list(enumerate(validDict)))
print([x for x in enumerate(validDict)])
print(list(zip(enumerate(validDict))))
print(any(x in s for x in validDict))
# s = s.replace(validDict[1],'')
# print(s)