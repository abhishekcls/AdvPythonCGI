class GrandParent:
    def __init__(self):
        print("GrandParent constructor called")
    def money(self):
        print("GrandParent's Money")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        print("Parent constructor called")
        
    def money(self):
        super().money()
        print("Parent's Money")

    def food(self):
        print("Parent's Food")

# Child class
class Child(Parent):#Multiple inheritance
    def __init__(self):
        super().__init__()
        print("Child constructor called")
    def money(self):#overriding
        super().money()
        print("Child's Money")

# Create Child object
s = Child()
s.money()
s.food()
print("======")
#f=Parent()