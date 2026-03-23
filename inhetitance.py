class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()

# Parent class
class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

# Child class
class Child(Parent):
    def __init__(self, name, roll_no):
        super().__init__(name)   # call parent constructor
        self.roll_no = roll_no
        print("Child constructor called")

# Create object
s = Child("Rahul", 101)

print(s.name)
print(s.roll_no)