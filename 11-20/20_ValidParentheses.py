def isValid(s):
    validDict = ["[]","()","{}"]
    while any(x in s for x in validDict):
        for i in range(3):
            if validDict[i] in s:
                s = s.replace(validDict[i],'')
    if s == '':
        return True
    else:
        return False

"""字典匹配"""
"""有改进余地，以后再看"""