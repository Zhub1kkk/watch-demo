# 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# 2
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 3
for i in range(1, 8):
    if i == 5:
        continue
    print(i)

# 4
nums = [-3, 4, -1, 7, -2]
for x in nums:
    if x < 0:
        continue
    print(x)


# 5
words = ["hi", "", "python", "", "ok"]
for w in words:
    if w == "":
        continue
    print(w)
