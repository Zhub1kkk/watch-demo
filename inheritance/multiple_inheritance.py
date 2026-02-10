# 1
class Fly:
    def ability(self):
        print("Can fly")

class Swim:
    def ability(self):
        print("Can swim")

class Duck(Fly, Swim):
    pass


# 2
class Writer:
    def write(self):
        print("Writing")

class Reader:
    def read(self):
        print("Reading")

class Student(Writer, Reader):
    pass


# 3
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()   # A


# 4
class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling")

class Smartphone(Camera, Phone):
    pass
