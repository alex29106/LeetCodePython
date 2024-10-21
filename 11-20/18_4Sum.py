from collections import Counter


def fourSum(nums, target):
    nums.sort()
    x = nums[0]
    counter = 1
    index = 1
    while index < len(nums):
        if nums[index] == x:
            counter = counter + 1
            if counter > 4:
                nums.pop(index)
            else:
                index += 1
        else:
            x = nums[index]
            counter = 1
            index += 1
    del counter, index, x
    result = []
    if any(abs(n) >= abs(target) / 4 for n in nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                leftkey = j + 1
                rightkey = len(nums) - 1
                while leftkey < rightkey:
                    if nums[i] + nums[j] + nums[leftkey] + nums[rightkey] == target:
                        if [nums[i], nums[j], nums[leftkey], nums[rightkey]] not in result:
                            result.append([nums[i], nums[j], nums[leftkey], nums[rightkey]])
                        leftkey += 1
                        rightkey -= 1
                    elif nums[i] + nums[j] + nums[leftkey] + nums[rightkey] < target:
                        leftkey += 1
                    else:
                        rightkey -= 1
        return result
    else:
        return []


def fourSum2(nums, target):
    nums.sort()
    x = nums[0]
    counter = 1
    index = 1
    while index < len(nums):
        if nums[index] == x:
            counter = counter + 1
            if counter > 4:
                nums.pop(index)
            else:
                index += 1
        else:
            x = nums[index]
            counter = 1
            index += 1
    del counter, index, x
    if not any(abs(n) >= abs(target) / 4 for n in nums):
        return []
    counts = Counter(nums)
    result = []
    nums = [i for i in sorted(counts)]
    print(nums)
    for i in nums:
        print(result)
        if counts[i] > 1:
            if counts[(target - i * 2) / 2] > 1 and (target - i * 2) / 2 != i:
                if sorted([i, i, int((target - i * 2) / 2), int((target - i * 2) / 2)]) not in result:
                    result.append(sorted([i, i, int((target - i * 2) / 2), int((target - i * 2) / 2)]))
            leftkey = 0
            rightkey = len(nums) - 1
            num = target - i * 2
            while leftkey < rightkey:
                if nums[leftkey] + nums[rightkey] == num:
                    if nums[leftkey] != i and nums[rightkey] != i:
                        if sorted([i, i, nums[leftkey], nums[rightkey]]) not in result:
                            result.append(sorted([i, i, nums[leftkey], nums[rightkey]]))
                    leftkey += 1
                    rightkey -= 1
                elif nums[leftkey] + nums[rightkey] < num:
                    leftkey += 1
                elif nums[leftkey] + nums[rightkey] > num:
                    rightkey -= 1
        if counts[i] > 2:
            if counts[target - i * 3] and target - i * 3 != i:
                if sorted([i, i, i, target - i * 3]) not in result:
                    result.append(sorted([i, i, i, target - i * 3]))
        if counts[i] > 3:
            if target == i * 4:
                if [i, i, i, i] not in result:
                    result.append([i, i, i, i])

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            leftkey = j + 1
            rightkey = len(nums) - 1
            while leftkey < rightkey:
                if nums[i] + nums[j] + nums[leftkey] + nums[rightkey] == target:
                    if [nums[i], nums[j], nums[leftkey], nums[rightkey]] not in result:
                        result.append([nums[i], nums[j], nums[leftkey], nums[rightkey]])
                    leftkey += 1
                    rightkey -= 1
                elif nums[i] + nums[j] + nums[leftkey] + nums[rightkey] < target:
                    leftkey += 1
                else:
                    rightkey -= 1
    return result


print(fourSum([0,5,0,4,7,0,-5,4,4,5,-7,-7,0], -27))

"""四数之和"""
"""自行尝试数据预处理后，在数据预处理方面得出如下结论：
   1， 数据预处理可以分部进行，从区域入手，一步步处理
   2， 可以从简单的开始，如在x数之和中，先去除重复大于x的值，随后对列表进行是否可行的预估，本题在leetcode上通过这两步将运行时间从847降至263
   3， 通过对数据和算法的类型的经验进行专项预处理，注意，这种方式并不一定会带来正向的效果且及其需要经验。"""
"""本算法带的两个方法都可以使用，虽然第二个算法进行了更加复杂（石山代码）的预处理，但是
   在leetcode上的时间消耗反而比第一个要更多，且消耗了更多的内存空间，其本质是因为减少的n
   并没有比预处理所使用的时间要少。其原因可能是因为笔者的代码水平不过关，建议日后再来尝试"""
