# 1
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#   2
i = 0
while i < 10:
    i += 1
    if i == 4:
        break
    print(i)

# 3
nums = [1, 3, 5, 7, 9]
i = 0
while i < len(nums):
    if nums[i] == 5:
        break
    i += 1
print("Найдено число 5")


# 4
while True:
    n = int(input())
    if n == 0:
        break
    print(n)

# 5
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        break
    print("Попытка", attempts)
