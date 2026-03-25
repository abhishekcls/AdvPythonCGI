class Father:
    def __init__(self):
        print("Father constructor called")
        super().__init__()#It calls Mother when creating Child object
    def money(self):
        print("Father's Money")

class Mother:
    def __init__(self):
        print("Mother constructor called")
        super().__init__()
    def money(self):
        print("Mother's Money")
    def food(self):
        print("Mother's Food")

# Child class
class Child(Father,Mother):#Multiple inheritance actually Child -> Father -> Mother(internally its multilevel)
    def __init__(self):
        super().__init__()
        print("Child constructor called")
    def money(self):
        super().money()
        Mother().money()
        print("Child's Money")

# Create Child object
s = Child()
s.money()
s.food()
print("======")
f=Father()