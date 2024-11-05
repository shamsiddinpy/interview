s = "abcde"
goal = "abced"
# if len(s) != len(goal):
#     print(False)
# print(goal in (s + s))
print(len(s) == len(goal) and goal in s + s)
