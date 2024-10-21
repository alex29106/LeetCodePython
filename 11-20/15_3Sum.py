def threeSum(nums):
    nums.sort()
    outputs = []
    for i in range(len(nums)):
        basekey = i
        leftkey = basekey + 1
        rightkey = len(nums) - 1
        while leftkey < rightkey:
            if nums[leftkey] + nums[rightkey] == -nums[basekey]:
                if [nums[basekey], nums[leftkey], nums[rightkey]] not in outputs:
                    outputs.append([nums[basekey], nums[leftkey], nums[rightkey]])
                leftkey += 1
                rightkey -= 1
            elif nums[leftkey] + nums[rightkey] < -nums[basekey]:
                leftkey += 1
            else:
                rightkey -= 1

    return outputs

print(threeSum([-1,0,1,2,-1,-4]))

"""双指针算法"""
"""标准三数之和解答，通过锚定一个值，对其他的值进行双数之和，对其他值进行双数
   之和后，锚定第二个值并重复以上步骤，直到找到所有值。对于x数之和，其时间复杂
   度为O(n^(x-1))。但是，并不代表无法继续优化，对数据进行预处理在接下来的文件里"""