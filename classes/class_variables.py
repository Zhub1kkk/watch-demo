# 1
class School:
    name = "High School"


# 2
class User:
    count = 0

    def __init__(self):
        User.count += 1


# 3
class Car:
    wheels = 4

    def __init__(self, color):
        self.color = color


# 4
class Game:
    level = 1

print(Game.level)
g1 = Game()
print(g1.level)
