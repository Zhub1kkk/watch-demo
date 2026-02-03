# 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# 3
for i in range(1, 10):
    if i == 6:
        break
    print(i)

# 4
nums = [2, 4, 6, 8, 10]
for x in nums:
    if x == 6:
        break
    print(x)

# 5
for _ in range(100):
    s = input()
    if s == "stop":
        break
    print(s)
