class Demo:
    def __init__(self,name,desig):
        self.name=name
        self.desig=desig

    def __str__(self):
        return f"Name={self.name} Designation={self.desig}"

d=Demo("Abhishek","Trainer")
print(d)