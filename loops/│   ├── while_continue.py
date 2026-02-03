# 1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# 2
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# 4
nums = [-2, 5, -1, 7, -3]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# 5
while True:
    s = input()
    if s == "":
        continue
    print("Ввод:", s)
