# 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 2
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)


# 3
nums = [3, 10, 25, 7, 40]

big = list(filter(lambda x: x > 10, nums))

print(big)

# 4
grades = [95, 60, 45, 88, 30, 72]

passed = list(filter(lambda g: g >= 60, grades))

print(passed)
