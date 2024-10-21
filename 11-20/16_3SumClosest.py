from collections import Counter

def threeSumClosest(nums,target):
    nums.sort()
    dif = 5001
    output = []
    for i in range(len(nums)):
        basekey = i
        leftkey = basekey + 1
        rightkey = len(nums) - 1
        while leftkey < rightkey:
            if nums[leftkey] + nums[rightkey] == -nums[basekey]:
                if abs(target - (nums[basekey]+nums[leftkey]+nums[rightkey])) < dif:
                    dif = abs(target - (nums[basekey]+nums[leftkey]+nums[rightkey]))
                    output = [nums[basekey],nums[leftkey],nums[rightkey]]
                    leftkey += 1
                    rightkey -= 1
            elif nums[leftkey] + nums[rightkey] < -nums[basekey]:
                leftkey += 1
            else:
                rightkey -= 1

    return outputs

