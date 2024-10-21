def longestCommonPrefix(strs):
    prefix = strs[0]
    for i in range(len(strs)):
        if prefix != strs[i][:len(prefix)]:
            while prefix != strs[i][:len(prefix)]:
                prefix = prefix[:-1]
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))

"""无名"""
"""过于简单，自行理解"""
