# 1
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

# 2
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# 3
students = [
    ("Ali", 85),
    ("Dana", 92),
    ("Aruzhan", 78)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

# 4
products = [
    {"name": "Phone", "price": 300},
    {"name": "Laptop", "price": 900},
    {"name": "Tablet", "price": 450}
]

sorted_products = sorted(
    products,
    key=lambda item: item["price"],
    reverse=True
)

print(sorted_products)
