nums = [1, 3, 5, 6]
target = 5
n = len(nums) - 1
l = 0
while l <= n:
    m = (l + n) // 2
    if nums[m] < target:
        l = m + 1
    elif nums[m] > target:
        n = m - 1
    else:
        print(m)
print(l)
