# 1
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")


# 2
class Shape:
    def area(self):
        print("Unknown area")

class Square(Shape):
    def area(self):
        print("Area = side * side")


# 3
class Teacher:
    def work(self):
        print("Teaching")

class OnlineTeacher(Teacher):
    def work(self):
        print("Teaching online")


# 4
class Game:
    def start(self):
        print("Game started")

class Chess(Game):
    def start(self):
        print("Chess game started")
