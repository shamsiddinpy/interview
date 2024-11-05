# from math import gcd
#
# str1 = "ABCABC"
# str2 = "ABC"
# b = gcd(len(str1), len(str2))
# if b:
#     a = str1[:b]
#     print(a)
# else:
#     print(" ")
#


candies = [2, 3, 5, 1, 3]
extraCandies = 3

maxi = max(candies)  # 5
disk = []
for i in candies:
    a = i + extraCandies
    if a >= maxi:
        disk.append(True)
    else:
        disk.append(False)
print(disk)
