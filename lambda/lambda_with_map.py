# 1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# 2
nums = [1, 2, 3, 4, 5, 6]

even_odd = list(map(lambda x: "even" if x % 2 == 0 else "odd", nums))

print(even_odd)

# 3
celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

print(fahrenheit)

# 4
a = [1, 2, 3]
b = [4, 5, 6]

sum_lists = list(map(lambda x, y: x + y, a, b))

print(sum_lists)
