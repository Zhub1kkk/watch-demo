# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

# 2
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow")


# 3
class Account:
    def show(self):
        print("Account info")

class PremiumAccount(Account):
    def show(self):
        super().show()
        print("Premium features")


# 4
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()
