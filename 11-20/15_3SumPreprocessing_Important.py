from collections import Counter
from bisect import bisect_right


def threeSum(nums,target):
    nums.sort()
    """x等于第一个元素"""
    x = nums[0]
    """由于计算了x,所以计数器=1"""
    counter = 1
    """由于x是第一个元素，index从第二个元素开始"""
    index = 1
    """通过遍历nums，移除多余的重复元素。对于非零元素，最多保留两个；对于零元素，最多保留三个"""
    while index < len(nums):
        if nums[index] == x:
            """如果index的数字等于x，计数器进位"""
            counter = counter + 1
            """如果x是0，可以有3次"""
            if x == 0:
                if counter > 3:
                    nums.pop(index)
                else:
                    index += 1
            elif counter > 2:  #对于其他数值，只有两个，多余的会移除
                nums.pop(index)
                """如果等于两次，index进位"""
            else:
                index += 1
            """如果index的值不等于x，则x等于新的index的值，counter重置为1，index再进位"""
        else:
            x = nums[index]
            counter = 1
            index += 1
    """检查Nums中是否都为复数"""
    if (not all(n > 0 for n in nums)):
        counts = Counter(nums)
        """如果零的数量大于等于3，添加 [0, 0, 0] 到结果中并移除所有0和重复数"""
        result = [[0, 0, 0]] if counts[0] >= 3 else []
        nums = [i for i in sorted(counts) if i != 0]
        """如果原 nums 中包含零，检查是否存在 -i 和 i 的组合，使得 -i + 0 + i = 0"""
        if counts[0] > 0:  #counts[0]指counts中0的数量
            for i in nums:
                if i > 0:
                    break  #只循环负数，避免重复添加和多余的时间复杂度
                if -i in counts:
                    result.append([-i, 0, i])
        """对nums进行binary操作"""
        for i in nums:
            if i & 1:  #检查i是否是偶数，也就是对i的二进制模式的最后一位进行与操作，如果是奇数会返回1并跳过，偶数则返回0
                continue
            remaining = -i >> 1  #对i进行1个向右的移位，意思是除2
            if counts[remaining] >= 2:  #如果原 nums 中包含两个i的负一半，则添加到结果中
                result.append([i, remaining, remaining])
        """对剩下的nums进行三数之和"""
        for i, n in enumerate(nums):
            kk = -(nums[0] + n)
            if kk < n:
                break
            j = bisect_right(nums, -n << 1) if n < 0 else i + 1
            k = bisect_right(nums, kk)
            for right in nums[j:k]:
                left = -(n + right)
                if left in counts:
                    result.append([left, n, right])
        del counts, nums
        return result
    else:
        return []


"""全面数据预处理+三数之和双指针"""
"""非常全面的预处理，这段代码可能看着很长，但是对于大数据集，他的实际消耗的时间是比前一个文件要低的多的。
   其中原理便是数据预处理，如上注释所示，该算法对数据进行了如去重，检查对数，检查偶数等操作。其中的原理便是
   降低O(n^2)中的n，以上的预处理操作几乎都是时间复杂度为n或2，3n的操作，只要这些操作的时间消耗量小于减少的
   n对算法的提升，那么总体来讲就是降低了算法的时间消耗。对于时间复杂度越高的算法，对数据的预处理便越重要"""
"""最后的三数之和看不懂，以后有时间再看"""
