def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


"""双指针算法"""
"""通过将指针设置在头尾，他们的width必然是最大值，在area = height * width中，
   width从最大值不断递减，所以寻找更高的height成为了需要解决的问题，在算法中，
   如果左指针大于右指针，右指针便向内靠近一点，反之亦然，以此来寻找更高的height"""

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
